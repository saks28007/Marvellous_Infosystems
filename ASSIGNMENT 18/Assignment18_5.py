# Get file name and string to search from the user
filename = input("Enter the file name: ")
search_string = input("Enter the string to search: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        # Count occurrences of the string
        count = content.count(search_string)
        print(f"The string '{search_string}' appears {count} times in {filename}.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
