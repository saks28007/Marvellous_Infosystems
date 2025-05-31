from functools import reduce

# Q4: Calculate the product of all numbers using reduce() and lambda

# Taking input from the user
lst = list(map(int, input("Enter list: ").split()))

# Calculating the product using reduce and lambda
product = reduce(lambda x, y: x * y, lst)

# Displaying the result
print("Product:", product)
