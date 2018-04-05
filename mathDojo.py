class MathDojo(object):
	def __init__(self):
		self.total = 0
	def result(self):
 		print "The result is: " + str(self.number)
 		return self
 	def add(self, value1, value2):
 		self.total = value1 + value2
        return self
 	def substract(self, value2): 
 	  	self.number -= value2
 	  	return self

 	  	



math1 = MathDojo()
math2 = MathDojo()
math1.add(2).add(2,5).subtract(3,2).result


bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
#bike1.displayInfo()
#bike1.reverse()

# print bike1.displayInfo().ride()
# #.ride().ride().reverse().displayInfo()

#str()