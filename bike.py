class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
 		print "The price of car is: " + str(self.price) + " max speed is: " + str(self.max_speed) + " and the miles: " + str(self.miles)
 		return self
 	def ride(self):
 		self.miles = self.miles + 10
 	  	print "riding: " +  str(self.miles) 
 	  	return self 
 	def reverse(self): 
 	  	self.miles = self.miles - 5
 	  	print "reverse: " +  str(self.miles)  
 	  	return self

# What would you do to prevent the instance from having negative miles?
# def reverse(self):
# 	if self.miles >= 5:
#  		self.miles -= 5
#   print "Reversing...", self.miles
#   return self

bike1 = Bike(200, "25mph")
bike2 = Bike(500, "55mph")
bike3 = Bike(350, "65mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
#bike1.displayInfo()
#bike1.reverse()

# print bike1.displayInfo().ride()
# #.ride().ride().reverse().displayInfo()

#str()