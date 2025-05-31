# Q2. Vowel or Consonant Check

# Accept a single character from the user
char = input("Enter a character: ").lower()

# Check if input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
