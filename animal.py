class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health = self.health - 1
		return self
	def run(self):
		self.health = self.health - 5
		return self
	def displayHealth(self):
		print "The health of the animal " + self.name + " is: \n" + str(self.health)
		return self
#animal1 = Animal("zebra",200,)
#animal1.walk().walk().walk().run().run().displayHealth()
class Dog(Animal):
	def __init__(self, name, health)
        super(Dog, self).__init__(name, health):   
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self
#dog1 = Dog("dog",150)
#dog1.walk().walk().walk().run().run().displayHealth()
class Dragon(Animal):
	def __init__(self, name, health)
        super(Dragon, self).__init__(name, health):   
        self.health = 170
    def fly(self):
		self.health = self.health - 10
		return self
	def displayhealth(self):
		print "healh: ", self.health
		print "i am a dragon"
		return self
dragon1 = Dragon("Dragon", 170)
dragon1.walk().walk().walk().run().run().displayHealth()


animal1 = Animal("zebra",200)
dog1 = Dog("dog",150)
dragon1 = Dragon("Dragon", 170)

animal1.walk().walk().walk().run().run().displayHealth()
dog1.walk().walk().walk().run().run().displayHealth()
dragon1.walk().walk().walk().run().run().displayHealth()





