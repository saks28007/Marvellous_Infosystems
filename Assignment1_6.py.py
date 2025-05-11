#Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkNum(no):
    
    if no > 0:
        print("This is positive number.")
    
    elif no < 0:
        print("This is negative number.")

    else:
        print("This is zero.") 


print("Enter a number: ")
val = int(input())
ChkNum(val)

