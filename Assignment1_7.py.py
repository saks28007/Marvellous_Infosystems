#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def ChkDiv(no):
    if no%5 == 0:
        print("Number is divisible by 5.")
        return True
    else:
        print("Number is not divisible by 5.")
        return False 

print("Enter a number: ")
val = int(input())
ChkDiv(val)