# Q5: Check if a string is a palindrome

# Taking input from the user
string = input("Enter a string: ")

# Checking for palindrome
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
