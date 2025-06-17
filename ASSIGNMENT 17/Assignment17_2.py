import schedule
import time
from datetime import datetime

def task2():
    print("Current Date and Time:", datetime.now())

schedule.every(1).minutes.do(task2)

while True:
    schedule.run_pending()
    time.sleep(1)
