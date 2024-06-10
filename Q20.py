# 20. Write a python program that takes a list of numbers and returns their sum. 
print("Enter multiple lines of input. Write -1 to stop.")
num = int(input("Enter your number: "))
sum = 0
while (num != -1):
    sum = sum + num
    num = int(input("Enter your number: "))
print("The sum is:", sum)

