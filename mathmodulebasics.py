'''
name:Ageena Mathew
date:18-10-24
description:program that uses functions from the math module to perform the following operations on a number provided by the user
'''

import math
number=int(input('enter a number:'))
square_root=math.sqrt(number)
print("square root of ",number,":",square_root)
factorial_num=math.factorial(number)
print("factorial of",number,":",factorial_num)
power_num=math.pow(number,2)
print(number,"raised to the power of 2:",power_num)
