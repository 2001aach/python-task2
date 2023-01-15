#  3.Create a string from the given string where the first and last character are exchanged.

string=input("enter the word")
x=list(string)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))