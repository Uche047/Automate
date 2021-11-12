class Dog:
	""" A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.appelation = name
		self.age = age
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.appelation} is now sitting.")
	def roll_over(self):
		#Simulate rolling over in response to a command.
		print(f"{self.appelation} rolled over!")
my_dog = Dog('Bruno', 4)
your_dog = Dog('Bruno', 4)

print(f'My dog\'s name is {my_dog.appelation} yeah yeah and he is {my_dog.age} years old')
print('Your dog\'s name is' , your_dog.appelation, 'yeah and he is',  your_dog.age, 'years old')

my_dog.sit()
my_dog.roll_over()