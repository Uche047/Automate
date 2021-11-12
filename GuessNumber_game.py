import random
secretnumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
	print('Take a guess.')
	guess = int(input())
	
	if guess < secretnumber:
		print('Your guess is too low')
	elif guess > secretnumber:
		print('Your guess is too high.')
#	else:
		#break   # This condition is the correct guess
	if guess == secretnumber:
		print('Good job! You guessed my number in ' + str(guessesTaken) + '  guesses !')
		break
	else:
		print('Nope. That is not what I was thinking of')