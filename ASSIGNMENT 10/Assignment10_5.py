from functools import reduce

numbers = [2, 70, 11, 12, 17, 23, 31, 77]
filtered = list(filter(lambda x: x not in [2, 70, 31], numbers))
print("List after filter =", filtered)

mapped = list(map(lambda x: x * 2, filtered))
print("List after map =", mapped)

result = reduce(lambda x, y: x if x > y else y, mapped)  # Max value
print("Output of reduce =", result)
