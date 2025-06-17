import os

# Ask the user to enter the file name
filename = input("Enter the file name: ")

# Check if the file exists in the current directory
if os.path.exists(filename):
    print(f"{filename} exists in the current directory.")
else:
    print(f"{filename} does NOT exist in the current directory.")
