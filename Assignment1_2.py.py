#Write a program which contains one functions named as ChkNum() which accept one parameter as number. If number is even then it should display "Even Number" otherwise display "Odd number" on console.

def ChkNum(no):
    no = 0

    print("Enter a number: ")
    no = int(input())

    if no%2:
        print("Odd number")
    else:
        print("Even number")

    

i = 0
value = ChkNum(i)




