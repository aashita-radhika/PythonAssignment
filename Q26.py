# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
str= input("Enter your string: ")
print("1. Check for prefix")
print("2. Check for suffix")
choice = input("Enter your choice (1/2): ")
if (choice == 1):
    str1 = input("Enter starting string: ")
    if (str.lower().startswith(str1)):
        print("True")
    else:
        print("False")
elif (choice == 2):
    str2 = input("Enter ending string: ")
    if (str.lower().endswith(str2)):
        print("True")
    else:
        print("False")
else:
    print("Invalid Choice")
                