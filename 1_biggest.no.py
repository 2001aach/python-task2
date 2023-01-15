# 1. Find biggest of 3 numbers entered.

a=int(input("enter the first number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if a>b and a>c:
    largest=a
elif b>c:
    largest=b
else :
    largest=c
print(largest,"is the largest number")
