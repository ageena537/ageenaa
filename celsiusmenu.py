'''
author:ageena mathew
date:28-10-24
description: a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
'''
while True:
    print("\n1.\t Convert celsius to farenheit")
    print("\n2.\t convert farenheit into celsisus")
    print("\n3.\t Exit")
    choice=int(input("choose a convertion:"))
    if choice==1:
        temp = float(input("enter a temperature in celsius:"))
        print(temp,"in farenheit is",(temp * 9/5) + 32)
    elif choice==2:
        temp2_=float(input("enter a temperature in farenheit:"))
        print(temp2_,"in celsius is", (temp2_- 32) * 5/9)
    elif choice==3:
        break
    else:
        print("invalid entry")

