 # This program opens all txt files in a given specified folder in this case the Developper folder
 # Uses a user supplied regex to search for any lines in the text files
 # The matched results are then printed
# Necessary imports
from pathlib import Path
import re
# Path to folder
myPath = Path('C:/Users/patri/PycharmProjects/Developper')
# Creates a list of all txt files in folder using generator
myList = list(myPath.glob('*.txt'))
# Request for user input
userRegex = input('Pls input your regex for the txt files: ')
Regex = re.compile(userRegex)

result  = []
# Looping through all txt files
for file in myList:
	check = open(file, 'r')
	List = check.readlines()
	check.close()
	# Checking lines for matches
	for line in List:
		match = Regex.findall(line)
		# Adding matches to a list
		for item in match:
			result.append(item)
# Displays the matches
if result:
        print(result)
else:
        print('Sorry no match')




