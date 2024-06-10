# 5. Write a program that takes a string input from the user and writes it to a text file. 
file = open("TextFile.txt", "w")
str = input("Enter your string:\n" )
file.write(str)
print("The string has been written in the text file")