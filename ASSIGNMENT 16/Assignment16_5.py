filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        for line in file:
            if len(line.split()) > 5:
                print(line.strip())
except FileNotFoundError:
    print("File not found.")
