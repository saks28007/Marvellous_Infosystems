import threading

# Function to count lowercase letters
def count_small_chars(text):
    count = sum(1 for c in text if c.islower())
    print(f"[{threading.current_thread().name} | ID: {threading.get_ident()}] Lowercase count: {count}")

# Function to count uppercase letters
def count_capital_chars(text):
    count = sum(1 for c in text if c.isupper())
    print(f"[{threading.current_thread().name} | ID: {threading.get_ident()}] Uppercase count: {count}")

# Function to count digit characters
def count_digits(text):
    count = sum(1 for c in text if c.isdigit())
    print(f"[{threading.current_thread().name} | ID: {threading.get_ident()}] Digit count: {count}")

if __name__ == "__main__":
    input_string = input("Enter a string: ")

    # Create threads with names
    small_thread = threading.Thread(target=count_small_chars, args=(input_string,), name="Small")
    capital_thread = threading.Thread(target=count_capital_chars, args=(input_string,), name="Capital")
    digits_thread = threading.Thread(target=count_digits, args=(input_string,), name="Digits")

    # Start threads
    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    # Wait for all threads to finish
    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Main thread: All threads completed.")
