def sum_of_elements(lst):
    return sum(lst)

def main():
    n = int(input("Number of elements: "))
    elements = []
    for i in range(n):
        elements.append(int(input("Enter element: ")))
    result = sum_of_elements(elements)
    print("Output:", result)

if __name__ == "__main__":
    main()
