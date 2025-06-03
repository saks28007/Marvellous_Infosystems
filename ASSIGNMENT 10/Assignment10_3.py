from functools import reduce

numbers = [4, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
filtered = list(filter(lambda x: x >= 70 and x <= 100, numbers))
print("List after filter =", filtered)

mapped = list(map(lambda x: x + 10, filtered))
print("List after map =", mapped)

result = reduce(lambda x, y: x * y, mapped)
print("Output of reduce =", result)
