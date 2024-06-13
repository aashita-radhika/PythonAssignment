# 19. Write a python program that removes all punctuation from a given string. 
import string
str= input("Enter your string: ")
translator = str.maketrans('', '', string.punctuation)
print("Original string:", str)
print("String without punctuation:", str.translate(translator))
