filename = input("Enter file name: ")
search_string = input("Enter the string to search: ")

try:
    with open(filename, 'r') as file:
        contents = file.read()
        count = contents.count(search_string)
        print(f"The string '{search_string}' occurred {count} time(s) in {filename}.")
except FileNotFoundError:
    print("File not found.")
