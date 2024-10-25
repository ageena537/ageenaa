'''
author:ageena mathew
date:25-10-24
description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
'''
var1=int(input("enter a temperature:"))
var2=input("Is this in (C)elsius or (F)ahrenheit?")
if var2=="F":
    print (var1,"farehnheit is",5/9*(var1-32),"celsius")
else:
    print(var1,"celsius is",(9/5*var1)+32,"farenheit")