import os

os.system('net user > outFile.txt')

linesOfData = []
with open('outFile.txt', 'r') as inFile:
	linesOfData = inFile.readlines()
	
#here you can either load the search manually or from a file, I'll do it from a file for our purposes

targets = []
with open('searchfile.txt', 'r') as inFile:
	targets = inFile.readlines()
	
for i in range(len(targets)):
	for j in range(len(linesOfData)):
		if targets[i] in linesOfData[j]:
			#add data to wherever you want it to go outfile print on screen etc

# os.system('rm outFile.txt')
