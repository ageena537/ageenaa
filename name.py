'''
author:ageena mathew
date:19-10-24
description:Create, concatenate, and print a string and access a sub-string from a given string.
'''
name1=input("enter your first name:")
last1=input("enter your last name:")
name=name1+" "+last1
print(name)
name_length=len(name1)
print(name_length)
extraction=name[name_length+1:]
print(extraction)
