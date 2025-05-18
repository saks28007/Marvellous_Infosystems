from MarvellousNum import ChkPrime

def ListPrime(lst):
    return sum(num for num in lst if ChkPrime(num))

def main():
    n = int(input("Number of elements: "))
    elements = []
    for i in range(n):
        elements.append(int(input("Enter element: ")))
    result = ListPrime(elements)
    print("Output:", result)

if __name__ == "__main__":
    main()
