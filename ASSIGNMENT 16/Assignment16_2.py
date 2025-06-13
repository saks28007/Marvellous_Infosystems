try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("data.txt not found.")
