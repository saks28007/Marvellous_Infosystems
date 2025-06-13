import sys

if len(sys.argv) < 2:
    print("Usage: python script.py source_file.txt")
else:
    source_file = sys.argv[1]
    destination_file = "Demo.txt"

    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Copied contents from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print("Source file not found.")
