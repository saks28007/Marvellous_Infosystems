def sum_of_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
