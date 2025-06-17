import schedule
import time
from datetime import datetime

def write_time_to_file():
    with open("Marvellous.txt", "a") as file:
        file.write(f"Current Time: {datetime.now()}\n")

# Schedule the task to run every 5 minutes
schedule.every(5).minutes.do(write_time_to_file)

while True:
    schedule.run_pending()
    time.sleep(1)
