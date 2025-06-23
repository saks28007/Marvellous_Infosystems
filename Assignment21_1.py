# ProcInfo.py

import psutil

def get_all_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def display_processes(processes):
    print(f"{'PID':<10} {'Name':<25} {'Username'}")
    print("-" * 50)
    for proc in processes:
        print(f"{proc['pid']:<10} {proc['name']:<25} {proc['username']}")

def main():
    try:
        processes = get_all_process_info()
        display_processes(processes)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
