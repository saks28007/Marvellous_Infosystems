filename = input("Enter file name: ")
try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("File not found.")
