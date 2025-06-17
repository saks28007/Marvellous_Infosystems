import schedule
import time

def check_email():
    print("Checking mail...")

# Schedule the task to run every 10 seconds
schedule.every(10).seconds.do(check_email)

while True:
    schedule.run_pending()
    time.sleep(1)
