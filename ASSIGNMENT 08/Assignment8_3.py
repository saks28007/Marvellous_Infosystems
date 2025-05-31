import threading

# Function to sum even numbers in a list
def sum_even_elements(numbers):
    total = sum(num for num in numbers if num % 2 == 0)
    print(f"EvenList Thread: Sum of even numbers = {total}")

# Function to sum odd numbers in a list
def sum_odd_elements(numbers):
    total = sum(num for num in numbers if num % 2 != 0)
    print(f"OddList Thread: Sum of odd numbers = {total}")

if __name__ == "__main__":
    # Example input list
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create threads
    even_thread = threading.Thread(target=sum_even_elements, args=(input_list,), name="EvenList")
    odd_thread = threading.Thread(target=sum_odd_elements, args=(input_list,), name="OddList")

    # Start threads
    even_thread.start()
    odd_thread.start()

    # Wait for threads to complete
    even_thread.join()
    odd_thread.join()

    print("Main thread: Both threads have completed.")
