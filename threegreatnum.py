'''
description:Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and num1>num3:
    print(num1,"is greater than other two")
elif num2>num3:
    print(num2,"is greater than other two")
else:
    print(num3,"is greater than other two")