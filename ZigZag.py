import time, sys
indent = 0 # How many spaces to indent
indentIncrease = True

try:
	while True:
		print(' ' * indent, end='')
		print('Dance!Dance!')
		time.sleep(0.4)
		
		if indentIncrease:
			indent +=1
			if indent == 20:
				# Change direction
				indentIncrease = False
		else:
			indent -=1
			if indent == 0:
				indentIncrease = True
except KeyboardInterupt:
	sys.exit()
			