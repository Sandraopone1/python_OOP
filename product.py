

class product(object):
	def __init__(self,price,itemName,weight,brand,status):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.status = status
		#self.tax = 0.15

	def sell(self):
		self.status = "sold"
		return self
	def addTax(self,tax):
		self.price = (self.price * tax) + self.price
		return self

	def returnItem(self,reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		if reason == "with box":
				self.status = "Like New"
		if reason == "without box":
				self.status = "used"
				self.price = (self.price * 20)/100

		return self

	def displayInfo(self):
		print "price: " + str(self.price) + " item name: " + str(self.itemName) + " weight: " + str(self.weight) + " brand: " + str(self.brand) + " status: " + str(self.status)
		return self

product1 = product(500,"dress",20,"oldNavy","for sale")


product1.sell().addTax(.10).displayInfo()
#product1.sell().addTax(.10).returnItem("defective").displayInfo()
# product1.returnItem("defective")
# # product1.displayInfo()
# product1.displayInfo()
# #product1.displayInfo()
# #product1.sell()