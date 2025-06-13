filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        contents = file.read()
        lines = contents.splitlines()
        words = contents.split()
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {len(contents)}")
except FileNotFoundError:
    print("File not found.")
