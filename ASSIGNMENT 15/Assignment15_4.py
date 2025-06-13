import sys

if len(sys.argv) < 3:
    print("Usage: python script.py file1.txt file2.txt")
else:
    file1, file2 = sys.argv[1], sys.argv[2]

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            if f1.read() == f2.read():
                print("Success: Both files have the same contents.")
            else:
                print("Failure: Files have different contents.")
    except FileNotFoundError:
        print("One or both files not found.")
