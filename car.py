class Car:
	# A simple attempt to represent a car.
	def __init__(self, make, model, year):
		#Initialize attributes to describe a car.
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 69
		self.filling = 0
	

	def get_descriptive_name(self):
		# Return a neatly formatted descriptive name.
		long_name = f"{self.year} {self.make} {self.model}" 
		return long_name.title()
	def read_odometer(self):
		# Print a statement showing the car's mileage.
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		# Set the odometer reading to the given value
		# Reject the change if it attempts to roll the odometer back .
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		# Add the given amount to the odometer reading
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")
		
	def fill_gas_tank(self, litres):
		if litres <= 20000:
			if self.filling < 20000:
				self.filling += litres
				print(f"The car currently is filled up to {self.filling}litres")
			elif self.filling + litres > 20000:
				print("Sorry you can't add that much of gas to the tank")
		else:
			print('You are not allowed to fill the car more than 20000litres')

class Battery:
	# A simple attempt to model a battery for an electric car.

	def __init__(self, battery_size=75):
		# Initialize the battery's attributes.
		self.battery_size = battery_size
	def describe_battery(self):
		# Print a statement describing the battery size.
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		#Print a statement about the range this battery provides.
		if self.battery_size == 75:
			carRange = 260
		elif self.battery_size == 100:
			carRange = 315
		print(f"This car can go about {carRange} miles on a full charge.")
			



class ElectricCar(Car):
	# Represents aspects of a car, specific to electric vehicles.

	def __init__(self, make, model, year):
		# Initialize attributes of the parent class.
		super().__init__(make, model, year)
		# Making the battery instance an attribute 
		# A new instance of Battery with a default size of 75 is created
		self.battery = Battery()
	def fill_gas_tank(self, litres):
		# Electric cars don't have gas tanks
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model u', 2020)
print(my_tesla.get_descriptive_name())
battery_1 = Battery(97)
battery_1.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




'''
my_tesla.describe_battery()
my_tesla.fill_gas_tank(20000) 
my_tesla.fill_gas_tank(2000)
'''
'''
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_used_car = Car('RangeRover', 'Sport', '2016')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

y = int(input("Pls input your odometer increment: "))

my_used_car.increment_odometer(y)
my_used_car.read_odometer()
'''