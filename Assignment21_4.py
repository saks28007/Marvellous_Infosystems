# ProcInfoLog.py

import os
import sys
import psutil
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Fetch all running processes
def get_all_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

# Write log to file
def write_log_to_file(directory, process_info):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"process_log_{timestamp}.txt"
        log_path = os.path.join(directory, filename)

        with open(log_path, 'w') as f:
            f.write(f"{'PID':<10} {'Name':<25} {'Username'}\n")
            f.write("-" * 50 + "\n")
            for proc in process_info:
                f.write(f"{proc['pid']:<10} {proc['name']:<25} {proc['username']}\n")

        print(f"Log file created at: {log_path}")
        return log_path
    except Exception as e:
        print(f"Error writing log file: {e}")
        return None

# Send log file via email
def send_email(log_path, recipient_email):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Process Log File'
        msg['From'] = 'your_email@gmail.com'            # <-- Replace this
        msg['To'] = recipient_email
        msg.set_content("Attached is the process log file.")

        with open(log_path, 'rb') as f:
            file_data = f.read()
            filename = os.path.basename(log_path)
            msg.add_attachment(file_data, maintype='text', subtype='plain', filename=filename)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@gmail.com', 'your_app_password')  # <-- Replace with your Gmail app password
            smtp.send_message(msg)

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function
def main():
    if len(sys.argv) != 3:
        print("Usage: python ProcInfoLog.py <DirectoryName> <EmailID>")
        return

    directory = sys.argv[1]
    email = sys.argv[2]

    processes = get_all_process_info()
    log_path = write_log_to_file(directory, processes)

    if log_path:
        send_email(log_path, email)

if __name__ == "__main__":
    main()
