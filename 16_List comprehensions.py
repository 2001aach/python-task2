#16. List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal
# values)

# (b) Square of N numbers
# n = 1
# while n <= 5:
#     print(n, '\t', n ** 2)
#     n += 1


# (c) Form a list of vowels selected from a given word
elem = input("Enter any word : ")
vowels =['a','e','i','o','u']
list1=[]
for x in elem:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given word : ",list1)

#(d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal values)
# word = "Hello"
# for character in word:
#     print(ord(character))

