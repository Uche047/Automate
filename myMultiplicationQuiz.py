#multiplication quiz program that gives score out of 10 
import time, random
numberOfQuestions = 10
correctAnswers = 0
# Looping through to ask 10 questions
for questionNumber in range(numberOfQuestions):
	# Pick two random numbers:
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)
	prompt = '*%s: %s x %s = ' %(questionNumber, num1, num2)
	tries = 0
	exceptTry = 0
	# Used to make sure that correct answers supplied after 8 seconds are returned invalid or incorrect
	timeOut = time.time() + 8
	while True:
			answer = input(prompt)
			tries += 1
			exceptTry += 1
			try:
				answer = int(answer)
				if answer == num1 * num2:
					# printing incorrect for answers although correct but have taken more than 8 seconds to be answered
					if timeOut < time.time():
						print ('incorrect')
						time.sleep(1)
						break
					else:
						print('correct')
						time.sleep(1)
						correctAnswers += 1
						break
				if answer != num1 * num2:
					if tries < 3:
						print('Try again')
						continue
					else:
						print ('out of tries')
						break
			except:
					#  To account for invalid input or non-integers
					if exceptTry < 3:
						print ('Only numeric values that are integers are allowed e.g 2, 3 ,5 etc : ')
					else:
						print ('out of tries')
						break
print ('Score %s / %s' %(correctAnswers, numberOfQuestions))	 	
	
		