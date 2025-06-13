try:
    with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
        dest.write(src.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("source.txt not found.")
