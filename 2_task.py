# . Accept an integer n and compute n+nn+nnn.
# [Hint : n = 5, then compute 5 + 55 + 555]

n=int(input("enter a number"))
num=str(n)
n1=num+num
n2=num+num+num
compute=n+int(n1)+int(n2)
print("The valu is:",compute )
