# 13. Write a program that asks the user for their birth year and calculates their age. 
import datetime
dob = int(input("Enter you year of birth: "))
current_year = datetime.datetime.now().year
age = current_year - dob
print("Your age is:", age)