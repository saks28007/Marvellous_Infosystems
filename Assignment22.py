# DuplicateFileRemoval.py

import os
import sys
import hashlib
import time
import smtplib
from datetime import datetime
from email.message import EmailMessage

def compute_checksum(file_path):
    h = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
    except Exception as e:
        return None
    return h.hexdigest()

def find_and_remove_duplicates(directory, log_dir):
    checksums = {}
    duplicates = []
    total_files = 0

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            total_files += 1
            checksum = compute_checksum(filepath)

            if checksum is None:
                continue

            if checksum in checksums:
                duplicates.append(filepath)
                try:
                    os.remove(filepath)
                except Exception as e:
                    continue
            else:
                checksums[checksum] = filepath

    # Create log
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_path = os.path.join(log_dir, log_name)

    with open(log_path, 'w') as log_file:
        log_file.write(f"Scan started at: {datetime.now()}\n")
        log_file.write(f"Total files scanned: {total_files}\n")
        log_file.write(f"Total duplicates found and removed: {len(duplicates)}\n")
        log_file.write("\nDeleted duplicate files:\n")
        for file in duplicates:
            log_file.write(f"{file}\n")

    return log_path, total_files, len(duplicates)

def send_email(log_file, recipient_email):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Duplicate File Removal Report'
        msg['From'] = 'your_email@gmail.com'  # Replace with your email
        msg['To'] = recipient_email
        msg.set_content("Attached is the duplicate file removal log report.")

        with open(log_file, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=os.path.basename(log_file))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@gmail.com', 'your_app_password')  # Replace with App Password
            smtp.send_message(msg)

        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <EmailID>")
        return

    directory = sys.argv[1]
    interval = int(sys.argv[2])
    email = sys.argv[3]

    if not os.path.isdir(directory):
        print("Error: Provided path is not a valid directory.")
        return

    log_dir = os.path.join(os.getcwd(), "Marvellous")

    while True:
        log_file, total, dup = find_and_remove_duplicates(directory, log_dir)
        send_email(log_file, email)
        print(f"Waiting {interval} minutes before next scan...")
        time.sleep(interval * 60)

if __name__ == "__main__":
    main()
