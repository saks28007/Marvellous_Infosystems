# ProcInfo.py

import psutil
import sys

def get_all_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def get_process_info_by_name(name):
    matches = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name'].lower() == name.lower():
                matches.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return matches

def display_processes(processes):
    if not processes:
        print("No matching processes found.")
        return

    print(f"{'PID':<10} {'Name':<25} {'Username'}")
    print("-" * 50)
    for proc in processes:
        print(f"{proc['pid']:<10} {proc['name']:<25} {proc['username']}")

def main():
    try:
        if len(sys.argv) == 1:
            # Show all processes
            processes = get_all_process_info()
            display_processes(processes)
        elif len(sys.argv) == 2:
            # Show specific process info
            proc_name = sys.argv[1]
            matches = get_process_info_by_name(proc_name)
            display_processes(matches)
        else:
            print("Usage:\n  python ProcInfo.py              # Show all processes\n  python ProcInfo.py <ProcName>  # Show specific process")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
