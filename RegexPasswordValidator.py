def passwordCheck(password):
	import re, pyinputplus
	if len(password) < 8:
		return 'password too short'
	myRegex = re.compile(r'[a-z]+[A-Z]+\d+|\d+[A-Z]+[a-z]+|[A-Z]+[a-z]+\d+')
	check = myRegex.search(password)
	if check is not None:
		return 'valid password'
	else:
		 return 'Invalid password'
f = 'ff11hh66666558hh1'
print(passwordCheck(f))