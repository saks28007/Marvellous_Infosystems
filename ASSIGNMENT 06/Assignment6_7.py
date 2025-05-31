# Q7. Accept 5 numbers from the user and find the maximum

# Accept input from the user
numbers = input("Enter 5 numbers separated by space: ").split()

# Convert input strings to integers
numbers = [int(num) for num in numbers]

# Find the maximum number
maximum = max(numbers)

# Print the result
print("Maximum number is:", maximum)
