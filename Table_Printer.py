def printTable(table):
	colWidth =[0] * len(table)
	for i in range(len(table)):
		for item in table[i] :
			if (colWidth[i]) < len(item):
				colWidth[i] = len(item)
		print(colWidth)
	for k in range(len(table[0])):
		for i in range(len(table)):
			print(table[i][k].rjust(colWidth[i]), end = ' ')
		print ()
			
tableData = [['apples', 'oranges', 'cherries','banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
