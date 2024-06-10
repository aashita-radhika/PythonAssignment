# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 
lines = []
print("Enter multiple lines of input. Press Enter on an empty line to stop.")
while True:
    line = input()
    if not line:
        break
    lines.append(line)

print("\nLines entered by the user:")
for line in lines:
    print(line)
