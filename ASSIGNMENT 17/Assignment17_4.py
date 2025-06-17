import schedule
import time

def greet():
    print("Namaskar...")

# Schedule the task to run every day at 9:00 AM
schedule.every().day.at("09:00").do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)
