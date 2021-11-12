def isValidChessBoard(x):
	white_count =black_count=wpawn_count =bpawn_count=wking_count=bking_count = 0
	word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	for  value in x.values():
		if value[0] == 'W':
			white_count += 1
		elif value[0] == 'B':
			black_count += 1
		if value == 'Wking':
			wking_count += 1
		elif value == 'Bking':
			bking_count += 1
		if value == 'Wpawn':
			wpawn_count += 1
		elif value == 'Bpawn':
			bpawn_count += 1
	if white_count > 16 or black_count > 16:
		print ('Invalid Chessboard')
		return False
	if wking_count > 1 or bking_count > 1:
		print ('Invalid Chessboard')
		return False
	if wpawn_count > 8 or bpawn_count > 8:
		print('Invalid Chessboard')
		return False
	for key in x.keys():
		if int(key[0]) > 8 or key[1] not in word_list:
			print('Invalid Chessboard')
			return False
	print('Valid Chessboard')
	return True

x = {'1a': 'Wking', '1b':'Wqueen', '1c':'Wrook', '1d': 'Wbishop', '1e':'Wknight', '1f' :'Wbishop', '1g':'Wrook', '1h':'Wknight' ,  '2a': 'Wpawn', '2b':'Wpawn', '2c':'Wpawn', '2d':'Wpawn', '8a':'Bking', '8b':'Bqueen', '8c':'Brook', '8d':'Bbishop','8e':'Bknight', '8f':'Bbishop', '8g':'Brook', '8h':'Bknight', '7a':'Bpawn', '7b':'Bpawn', '7c':'Bpawn', '7d':'Bpawn' }	
isValidChessBoard(x)