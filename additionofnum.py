'''
author:ageena mathew
date:25-10-24
desc:sum of digits of a number
'''
number=int(input("enter a number:"))
sum_of_digits=0
while number>0:
    remainder=number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
print("sum of given digits of thr given number is:",sum_of_digits)