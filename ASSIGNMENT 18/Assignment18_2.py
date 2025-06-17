# Ask the user to enter the file name
filename = input("Enter the file name: ")

try:
    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()
        print("File Contents:\n")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
