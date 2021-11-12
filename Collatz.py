def collatz(number):
	if number % 2 == 0:
		print(number//2) 
		return (number//2)
	if number % 2 == 1:
		print(3 * number + 1)
		return ( 3 * number + 1)
import sys
while True:
	try:
		d= int(input())
		break
	except ValueError:
		print("Pls type in a number")
		continue
while d != 1:
	d = collatz(d)
				

	