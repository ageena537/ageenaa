'''
author:ageena mathew
desc:find whether a number is armstrong or not
'''
var=int(input("enter a number"))
sum=0

while var>0:
    remainder=sum%10
    sum=remainder**3+sum
    var=var//10
if sum==var:
    print("The given number is armstrong number")
else:
    print("The given number is not armstrong number")