import schedule
import time
from datetime import datetime

def backup_files():
    with open("backup_log.txt", "a") as log_file:
        log_file.write(f"Backup completed at: {datetime.now()}\n")
    print("Backup done at", datetime.now())

# Schedule the backup task to run every hour
schedule.every().hour.do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(1)
