def frequency(lst, search):
    return lst.count(search)

def main():
    n = int(input("Number of elements: "))
    elements = []
    for i in range(n):
        elements.append(int(input("Enter element: ")))
    search = int(input("Element to search: "))
    result = frequency(elements, search)
    print("Output:", result)

if __name__ == "__main__":
    main()
