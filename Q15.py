# 15. Write a program that reads data from a CSV file and prints it to the console
import csv 
def read(): 
    with open("data.csv","r") as f: 
        rec = csv.reader(f)  
    for i in rec: 
          print(i) 
 
read() 