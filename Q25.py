# 25. Write a program that copies the contents of one text file to another. 
with open('TextFile.txt','r') as firstfile, open('second.txt','w') as secondfile: 
	for line in firstfile: 
			
			# write content to second file 
			secondfile.write(line)
