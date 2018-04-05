# class MathDojo(object):
# 	def __init__(self):
# 		self.total = 0
# 	def result(self):
#  		print "The result is: " + str(self.number)
#  		return self
#  	def add(self, value1, value2):
#  		self.total = value1 + value2
#         return self
#  	def substract(self, value2): 
#  	  	self.number -= value2
#  	  	return self

 	  	
class Call(object):
    def __init__(self, id, name, number, time, reason):
    	self.id = id
    	self.name = name
        self.number= number
        self.time = time
        self.reason = reason

    def display(self):
    	print "id: ", self.id, "name: ", self.name, "number: ", self.number, "time: ", self.time, "reason: ", self.reason

class Callcenter(object):
    def __init__(self, calls, calllist, number, time, reason):
    	self.id = id
    	self.name = name
        self.number= number
        self.time = time
        self.reason = reason

    def display(self):
    	print "id: ", self.id, "name: ", self.name, "number: ", self.number, "time: ", self.time, "reason: ", self.rea     
       


md = MathDojo()
md.add(1,(2,3),[4,5])



#bike1.displayInfo()
#bike1.reverse()

# print bike1.displayInfo().ride()
# #.ride().ride().reverse().displayInfo()

#str()