input_file = "file_with_blanks.txt"
output_file = "cleaned_file.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line)

print("Blank lines removed. Output saved in cleaned_file.txt")
