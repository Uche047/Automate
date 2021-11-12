myBoard = {
'top-Lf': ' ' , 'top-Mi': ' ', 'top-Ri': ' ',
'mid-Lf': ' ', 'mid-Mi': ' ', 'mid-Ri': ' ',
'low-Lf': ' ', 'low-Mi': ' ', 'low-Ri': ' ' }
def printBoard(board):
	print(board['top-Lf']  + '||' + board['top-Mi'] + '||' + board['top-Ri'])
	print('-<<->>-')
	print(board['mid-Lf']  + '||' + board['mid-Mi'] + '||' + board['mid-Ri'])
	print('-<<->>-')
	print(board['low-Lf']  + '||' + board['low-Mi'] + '||' + board['low-Ri'])
turn = 'X'
for i in range(9):
	printBoard(myBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	myBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(myBoard)
		