import zombiedice
class MyZombie:
	def __init__(self, name):
		#All zombies must have a name
		self.name = name
	def turn(self, gameState):
		# gameState is a dict with info about the current state of the game
		diceRollResults = zombiedice.roll() # first roll
		# roll() returns a dictionary with keys 'brains', 'shortgun', and
		# 'footsteps' with how many rolls of each type there were.
		# The 'rolls' key is a list of (color, icon) tuples with the
		# exact roll result information.
		# Example of a roll() return value
		#{'brains': 1, 'footsteps': 1, 'shotgun': 1, 'rolls': [('yellow', 'brains'), ('red', 'footsteps'), ('green', 'shotgun')]}
		# REPLACE THIS ZOMBIE CODE WITH YOUR OWN
		shotgun = brains = 0
		while diceRollResults is not None:
					shotgun += diceRollResults['shotgun']
					brains += diceRollResults['brains']
					if shotgun <= brains:
						diceRollResults = zombiedice.roll()
					else:
						break
					
zombies = (
		zombiedice.examples.RandomCoinFlipZombie(name='Random'),
		zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
		zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'Stop at 2 Shotguns', minShotguns= 1),
		MyZombie(name= 'My Zombie Bot'),
		# Add any other zombie players here
		)
# Uncomment one of the following lines to run in CLI or Web GUI mode
#zombiedice.runTournament(zombies = zombies, numGames = 1000)
zombiedice. runWebGui(zombies=zombies, numGames=1000)
