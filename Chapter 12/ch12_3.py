class Person:
	def __init__(self, n, g):
		self.name = n
		self.gender = g
	def display(self):
		print ("Name : ", self.n, ", Gender : ", self.g)
e1 = Person("Shikha", "Female")
e1.display()
