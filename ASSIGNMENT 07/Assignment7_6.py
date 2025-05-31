# Q6: Filter prime numbers using filter() and lambda

# Helper function to check for prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking input from the user
lst = list(map(int, input("Enter list: ").split()))

# Filtering prime numbers
prime_numbers = list(filter(is_prime, lst))

# Displaying the result
print("Prime numbers:", prime_numbers)
