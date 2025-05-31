import threading
import time

def print_numbers(thread_name):
    for i in range(1, 6):
        print(f"{thread_name}: {i}")
        time.sleep(1)

# Create three threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))
thread3 = threading.Thread(target=print_numbers, args=("Thread-3",))

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished.")
