#Write a program which contains one function named as Add() which accepts two nos. from user and return addition of that two numbers.

def Add(val1, val2):
    ans = 0

    ans = int(val1) + int(val2)

    print("Addition is : ",ans)

print("Enter first number :")
no1 = int(input())

print("Enter second number :")
no2 = int(input())

Add(no1, no2)

