# Save this as copy_to_demo.py
import sys

if len(sys.argv) != 2:
    print("Usage: python copy_to_demo.py <source_filename>")
    sys.exit(1)

source_file = sys.argv[1]
destination_file = "Demo.txt"

try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
        dst.write(src.read())
    print(f"Copied contents of {source_file} to {destination_file}")
except FileNotFoundError:
    print(f"{source_file} not found.")
