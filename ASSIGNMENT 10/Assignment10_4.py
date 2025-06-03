from functools import reduce

numbers = [5, 2, 3, 4, 1, 2, 8, 10]
filtered = list(filter(lambda x: x in [2, 4, 8, 10], numbers))
print("List after filter =", filtered)

mapped = list(map(lambda x: x ** 2, filtered))
print("List after map =", mapped)

result = reduce(lambda x, y: x + y, mapped)
print("Output of reduce =", result)
