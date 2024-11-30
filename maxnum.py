
'''
def maximum(numbers):
    print("the maximum of given numbers is:",max(numbers))

numbers=[]
for  i in range(3):
    num1=int(input("Enter the first number:"))
    numbers.append(num1)
maximum(numbers)
'''


def sumlist(list):

    print("The sum of list of the numbers is:",sum(list))
sumlist([1,34,56,77,9])
def  mult():
    list1=[8,2,3,-1,7]
    product=1
    for i in list1:
        product*=i
    print("The product of the given numbers is:",product)
mult()
def rev(str1):

    length=len(str1)
    print(str1[length::-1])
str1="1234abcd"
rev(str1)
