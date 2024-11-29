#Recursive function to multiply two positive numbers
def mult(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+mult(num1,num2-1)
num1=int(input("Enter positive number1:"))
num2=int(input("Enter positive number2:"))
print("The product of two numbers is :",mult(num1, num2))