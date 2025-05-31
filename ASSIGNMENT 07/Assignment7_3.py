# Q3: Filter even numbers using filter() and lambda

# Taking input from the user
lst = list(map(int, input("Enter list: ").split()))

# Filtering only even numbers using filter and lambda
even_numbers = list(filter(lambda x: x % 2 == 0, lst))

# Displaying the output
print("Even numbers:", even_numbers)
