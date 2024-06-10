# 3. Write a python program that calculates the factorial of a given number. 
num1 = int(input("Enter a number: "))
temp = num1
fact = 1
while (temp > 0):
    fact = fact * temp
    temp = temp - 1
print ("Factorial =", fact)
