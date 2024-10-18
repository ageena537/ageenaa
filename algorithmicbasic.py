'''
author:ageena mathew
date:18-10-24
description:Python program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results
'''

number1=int(input("enter a number:"))
number2=int(input("enter another number:"))
print("sum=",number1+number2,"division=",number1/number2)
print("Is number1 greater than number2?:",number1>number2)
print("Is number1 equal to number2:",number1==number2)
print("Logical AND:",number1>0 and number2>2)
print("Logical OR:",number1>number2 or number2>1)