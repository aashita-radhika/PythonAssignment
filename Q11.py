# 11. Write a python program that generates the first n numbers in the Fibonacci sequence. 
n=int(input("Number of Terms : ")) 
a = 0
b = 1 
i = 3
lst = [0, 1]

while i <= n: 
    c = a + b 
    lst.append(c)
    a = b
    b = c 
    i = i + 1
if (n > 0):
    print("The Fibonnaci sequence is:")
    if (n == 1):
        lst.pop()
    print(lst)
