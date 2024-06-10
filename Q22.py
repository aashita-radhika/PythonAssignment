# 22. Write a python program that returns the minimum and maximum values in a list of numbers.
print("Enter multiple lines of input. Write -1 to stop.")
num = int(input("Enter your number: "))
maximum = 0
minimum = 0
while (num != -1):
    maximum = max(num, maximum)
    minimum = min(num, minimum)
    num = int(input("Enter your number: "))
print("The maximum is:", maximum)
print("The minimum is:", minimum)

