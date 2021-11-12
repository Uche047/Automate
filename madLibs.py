# This code takes a text file reads it and prompts the user to replace key words and produces a new text file that is printed to screen and later is saved.
file = input('Pls input file in .txt format e.g bread.txt')

r = open(file, 'r')
fileList = list(r)

#print(fileList)
for item in fileList:
	if item == 'NOUN':
		noun = input('Pls enter a noun')
		fileList[fileList.index('NOUN')] = noun
		del fileList[fileList.index('NOUN') +1]
		


	elif item in fileList == 'ADJECTIVE':
		adjective = input('Pls enter an adjective')
		fileList[fileList.index('ADJECTIVE')] = noun
		del fileList[fileList.index('ADJECTIVE') +1]

	elif item in fileList == 'VERB':
		adjective = input('Pls enter a verb')
		fileList[fileList.index('VERB')] = noun
		del fileList[fileList.index('VERB') +1]

print(fileList)
myFile = open('newFile.txt', 'w')
myFile.write(str(fileList))


	
		
		




