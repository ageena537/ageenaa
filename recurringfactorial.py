def factorial(num):

    lim=1
    for i in range(1,num+1):
        lim=lim*i
    print("The factorial of the given number is:",lim)
num=int(input("Enter the number:"))
factorial(num)
