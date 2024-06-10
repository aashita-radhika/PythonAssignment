# 18. Write a python program that checks if two strings are anagrams of each other. 
str1 = input("Enter first string: " )
str2 = input("Enter second string: " )
a = sorted(str1.lower())
b = sorted(str2.lower())
if (a == b):
    print("The strings are Anagrams")
else:
    print("The strings are NOT Anagrams")
