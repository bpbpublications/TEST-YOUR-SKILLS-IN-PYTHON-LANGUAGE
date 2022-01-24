class Student:
    _school = 'Life School'

    def __init__(self, name, standard):
        self.name=name 
        self.standard=standard 

class UGStudent(Student):
    def __init__(self, name, standard,age):
        super().__init__(name, standard)
        self.age= age

s1 = Student("Steve", 7)
print("Details s1:")
print('School: ',s1._school)
print('Name: ',s1.name)
print('Standard: ',s1.standard)

s2= UGStudent("Smith", 7, 22)
print("Details s2:")
print('School: ',s2._school)
print('Name: ',s2.name)
print('Standard: ',s2.standard)
print('Age: ',s2.age)
