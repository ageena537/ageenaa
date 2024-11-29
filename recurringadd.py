def recursive_add(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)

num1=int(input("The first number:"))
num2=int(input("The second number:"))
recursive_add(num1,num2)
print("The sum of numbers is:",recursive_add(num1, num2))
