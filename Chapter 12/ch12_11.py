class Faculty:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age=age
    def displayInfo(self):
        print("Name: ", self.firstname, " " ,self.lastname, ", Age: ", self.age)
class Teacher(Faculty):
    def __init__(self, first, last, age, staffnum, subject):
        super().__init__(first, last,age)
        self.staffnumber = staffnum
        self.subject= subject

    def displayTeacher(self):
        super().displayInfo()
        print("Staff no.= ", self.staffnumber,", Subject = ", self.subject)

x = Faculty ("Usha", "Goel", 24)
y = Teacher ("Ramesh", "Goel", 34, 101, "Mathematics")
x.displayInfo ()
y.displayTeacher ()
 
