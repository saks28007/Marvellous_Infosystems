def inverted_triangle(n):
    for i in range(n):
        print(" " * i + "* " * (n - i))

def main():
    num = int(input("Enter number: "))
    inverted_triangle(num)

if __name__ == "__main__":
    main()
