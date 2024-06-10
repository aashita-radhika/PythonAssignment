# 12. Write a python program that calculates the sum of the digits of a given number. 
num = int(input ("Enter your number: "))
temp = num
sum = 0
while(temp >= 1):
    rem = int(temp % 10)
    sum = sum + rem
    temp = temp / 10
print("Sum of the digits:" , sum)