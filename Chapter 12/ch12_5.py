class KGStudent:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print ("Name : ", self.name, ", Marks: ", self.marks)

c1=KGStudent("Arnav", 100)
c1.display()