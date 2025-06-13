import os

filename = input("Enter file name: ")
if os.path.isfile(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")
