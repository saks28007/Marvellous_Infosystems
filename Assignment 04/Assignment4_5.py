from functools import reduce

Data = [2, 7, 10, 11, 17, 23, 31, 77]
FData = list(filter(lambda x: x % 2 == 1, Data))  # Odd numbers
MData = list(map(lambda x: x * 2, FData))
RData = reduce(lambda x, y: x if x > y else y, MData)   # Max function

print("List after filter =", FData)
print("List after map =", MData)
print("Output of reduce =", RData)
