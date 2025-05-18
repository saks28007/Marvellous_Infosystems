from functools import reduce

Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
FData = list(filter(lambda x: x % 2 == 0, Data))
MData = list(map(lambda x: x ** 2, FData))
RData = reduce(lambda x, y: x + y, MData)

print("List after filter =", FData)
print("List after map =", MData)
print("Output of reduce =", RData)
