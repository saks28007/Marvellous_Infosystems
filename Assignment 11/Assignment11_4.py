def power_iterative(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
