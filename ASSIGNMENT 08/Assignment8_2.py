import threading
import time

# Function for even number thread
def print_even():
    for i in range(2, 21, 2):  # First 10 even numbers
        print(f"EvenThread: {i}")
        time.sleep(0.1)  # Small delay for clarity

# Function for odd number thread
def print_odd():
    for i in range(1, 20, 2):  # First 10 odd numbers
        print(f"OddThread: {i}")
        time.sleep(0.1)  # Small delay for clarity

if __name__ == "__main__":
    # Create threads
    even_thread = threading.Thread(target=print_even, name="EvenThread")
    odd_thread = threading.Thread(target=print_odd, name="OddThread")

    # Start threads
    even_thread.start()
    odd_thread.start()

    # Wait for threads to complete
    even_thread.join()
    odd_thread.join()

    print("Both threads have finished execution.")
