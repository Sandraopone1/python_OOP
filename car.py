
class Car(object): 
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "\nnext Car\n" + "price: " + str(self.price) + "\nspeed: " + str(self.speed) + "\nFuel: " + str(self.fuel) + "\nMileage: " + str(self.mileage) + "\nTax: " + str(self.tax)   
	
	# def checkTax(self):
	# 	if self.price > 10000:
	# 		tax = 15%
	# 	else:
	# 		tax = 12%

car1 = Car(2000,55,"full",15)
car2 = Car(10000,35,"not full",15)
car3 = Car(3000,52,"full",15)
car4 = Car(40000,80,"not full",15)
car5 = Car(5000,60,"full",15)

# car1.__init__()