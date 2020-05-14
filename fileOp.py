path="Example.txt"


#to print whole file
with open(path,"r") as file:
	#firstLine=file.readline()
	#print(firstLine)
	fileContent=file.read()
	print(fileContent)
	
	
#print(file1.name)
#print(file1.mode)

#to print lines
file=open(path,"r")
print("***first line***")
print(file.readline())
file.close()

#another way to print line by line
file2=open(path,"r")
i=0
for line in file2:
	print(str(i)+":"+line)
	i=i+1
	
file.close()

#to get lines as list
print("*****the n'th line*****")
with open(path,"r") as file:
	FileAsList=file.readlines()
	print(FileAsList[2])
	
	
	
	
print("\n\n\nWriting starts\n\n")
def openFile(path):
	with open(path,"r") as file:
		print(file.read())
		
#to write to a file
path1="example2"
with open(path1,"w") as file:
	file.write("this is a\n")
	
openFile(path1)

#append to a file
with open(path1,"a") as file:
	file.write("this is b\n")
openFile(path1)
	
#copy from a list to a file

LineList={"this is x\n","this is y\n","this is z\n"}

with open("example3.txt","w") as file:
	for a in LineList:
		file.write(a)
		
openFile("example3.txt")


#copy contents of one file to another
with open(path,"r") as file1:
	with open("copyFile.txt","w") as file2:
		file2.write(file1.read())
		#for line in file1:
			#file2.write(line)
		
		
openFile("copyFile.txt")
