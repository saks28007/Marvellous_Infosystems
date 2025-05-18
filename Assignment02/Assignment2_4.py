def sum_of_factors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter number: "))
    print("Output:", sum_of_factors(num))

if __name__ == "__main__":
    main()
