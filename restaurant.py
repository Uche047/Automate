class Restaurant:
	""" A simple attempt to model a restaurant """
	def __init__(self, name, cuisine):
		self.restaurant_name = name
		self.cuisine_type = cuisine
		self.number_served = 0
	def describe_restaurant(self):
		"""Describe restaurants"""
		print(f"This is the prestigious restaurant {self.restaurant_name} and we delight our customers with various {self.cuisine_type}")
	def open_restaurant(self):
		# Shows restaurant is open business
		print(f"The {self.restaurant_name} restaurant is now open for business")
	def set_number_served(self, served):
		# Sets the number of customers served
		if served >= self.number_served:
			self.number_served = served
		else:
			print("The number of customers served is already greater than this value")
	def increment_number_served(self, increment):
		# Increments the number of customers served.
		if increment >= 0:
			self.number_served += increment
		else:
			print("Increment in customers must be positive value")

class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine):
		# Initialize attributes of parent class
		super().__init__(name, cuisine)	
		self.flavors = ["vanilla", "oreo", "sweet_cream", "peanut_butter","chocolate", "strawberry","popsicle","bubble_gum", "chilli_choclate","french_vanilla"]

	def display_flavors(self):
		for flavors in self.flavors:
			print(f"The {flavors}flavor is available.")
	

IceCreamStand_1 = IceCreamStand("ChopNowNow","African Dishes")
IceCreamStand_1.display_flavors()

# First instance
restaurant = Restaurant('ChopNowNow', 'African Dishes')
restaurant_1 = Restaurant('Calabar Kitchen', 'Local dishes')
restaurant_2 = Restaurant('KFC', 'Tenderly Fried Chicken')
restaurant_3 = Restaurant(' Iya Bas', 'Famed Nigerian Delicacies')

# Printing two attributes
print(f"This is the prestigous {restaurant.restaurant_name} restaurant")
print(f"We delight our customers with various {restaurant.cuisine_type}.")
# Calling two methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
# Calling describe_restaurant() method thrice
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# Changing an attribute value directly
restaurant.number_served = 50
# Changing an attribute using a method
restaurant.set_number_served(55)
# Updating an attribute value using a method
restaurant.increment_number_served(10)
# Printing the number of customers served
print(f"We have served {restaurant.number_served} customers so far")
