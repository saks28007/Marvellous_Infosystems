def max_in_list(lst):
    return max(lst)

def main():
    n = int(input("Number of elements: "))
    elements = []
    for i in range(n):
        elements.append(int(input("Enter element: ")))
    result = max_in_list(elements)
    print("Output:", result)

if __name__ == "__main__":
    main()
