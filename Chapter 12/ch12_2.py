class Human:
	def __init__(self, name, age):
		self.name = name
		self.salary = age
	def display(self):
		print ("Name : ", self.name, ", Age: ", self.age)

e1 = Human("Ashu", 30)
e1.display()
