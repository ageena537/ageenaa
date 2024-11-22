#creating a sorted list of odd and even
list1=[1,4,5,67,74]
list2=[32,45,6,3,87]
list_org=list1+list2
print("list 1:",list1)
print("list 2:",list2)
print("combined list:",list_org)
even=[]
odd=[]
for number in list_org:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
even.sort()
odd.sort()
print("after sorting:",even+odd)