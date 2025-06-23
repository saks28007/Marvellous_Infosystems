# ProcInfoLog.py

import os
import sys
from datetime import datetime
import psutil

def get_all_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

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
    except Exception as e:
        print(f"Error writing to log file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ProcInfoLog.py <DirectoryName>")
        return

    directory = sys.argv[1]
    processes = get_all_process_info()
    write_log_to_file(directory, processes)

if __name__ == "__main__":
    main()
