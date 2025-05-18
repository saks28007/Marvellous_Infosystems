from functools import reduce

Data = [34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
FData = list(filter(lambda x: x >= 70 and x <= 100, Data))
MData = list(map(lambda x: x * 10, FData))
RData = reduce(lambda x, y: x * y, MData)

print("List after filter =", FData)
print("List after map =", MData)
print("Output of reduce =", RData)
