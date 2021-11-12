def printTable(tableData):
	colWidth = [0] * len(tableData)
	for i in range(len(tableData)):
		for j in tableData[i]:
			if len(j) > colWidth[i]:
				colWidth[i] = len(j)
	'''
	length = 0
	for i in tableData:
		for j in i:
			if len(j) > length:
				length = len(j)
		'''		
	for x in range(len(tableData[0])):
		for i in range(len(tableData)):
			print(tableData[i][x].rjust(colWidth [i]), end = ' ')
		print()
			
tableData = [['apples', 'oranges', 'cherries','banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
