# Q2: Double each value using map() and lambda

# Taking input from the user
lst = list(map(int, input("Enter list: ").split()))

# Doubling each value using map and lambda
doubled = list(map(lambda x: x * 2, lst))

# Displaying the output
print("Doubled list:", doubled)
