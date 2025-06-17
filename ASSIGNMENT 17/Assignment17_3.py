import schedule
import time

def do_coding():
    print("Do Coding..!")

# Schedule the task to run every 30 minutes
schedule.every(30).minutes.do(do_coding)

while True:
    schedule.run_pending()
    time.sleep(1)
