# 6. Write a program that reads the content of a text file and prints it to the console. 
file = open("TextFile.txt", "r")
print("Contents of the file are: \n")
print(file.read())
