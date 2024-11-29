phonenum=input("enter your number:")
def number(phonenum):
'''
Function to checkif a mobile number is valid
:param number:mobile number
:return:True if number is valid,els false
'''
    if len(phonenum)==10 and phonenum[0] in "987":
        return True
    return False
if number(phonenum):
    print(f"The mobile number {phonenum} is valid")
else:
    print(f"The mobile number {phonenum} is not valid")