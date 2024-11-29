phonenum=input("enter your number:")
def number(phonenum):
    if len(phonenum)==10 and phonenum[0] in "987":
        return True
    return False
if number(phonenum):
    print(f"The mobile number {phonenum} is valid")
else:
    print(f"The mobile number {phonenum} is not valid")