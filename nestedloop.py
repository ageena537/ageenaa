
limit=int(input("enter the no.of rows:"))
print("increasing triangle")
for i in range(1,limit+1):
    for j in range(1):
        print("*"*i)

print("decreasing triangle")
for i in range(limit,0,-1):
    for j in range(1):
        print("*"*i)

print("hill pattern")
for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end="\t")
    for h in range(2*i-1):
        print("*",end="\t")
    print()

print("reverse hill pattern")
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end=" ")
    for h in range(2*i-1):
        print("*",end=" ")
    print()
