import schedule
import time

def lunch_time():
    print("Lunch Time!")

def wrap_up_work():
    print("Wrap up work")

# Schedule both tasks
schedule.every().day.at("13:00").do(lunch_time)     # 1:00 PM
schedule.every().day.at("18:00").do(wrap_up_work)   # 6:00 PM

while True:
    schedule.run_pending()
    time.sleep(1)
