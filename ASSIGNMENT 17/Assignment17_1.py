import schedule
import time

def task1():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(task1)

while True:
    schedule.run_pending()
    time.sleep(1)
