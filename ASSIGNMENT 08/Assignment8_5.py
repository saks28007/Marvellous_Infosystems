import threading
import time

# Function for Thread-1: prints 1 to 50
def print_ascending():
    for i in range(1, 51):
        print(f"Thread-1: {i}")
        time.sleep(0.01)  # Small delay for visibility

# Function for Thread-2: prints 50 to 1
def print_descending():
    for i in range(50, 0, -1):
        print(f"Thread-2: {i}")
        time.sleep(0.01)  # Small delay for visibility

if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=print_ascending, name="Thread-1")
    thread2 = threading.Thread(target=print_descending, name="Thread-2")

    # Start thread1 and wait for it to complete
    thread1.start()
    thread1.join()  # Ensures thread2 starts only after thread1 finishes

    # Now start thread2
    thread2.start()
    thread2.join()

    print("Main thread: Both threads have completed.")
