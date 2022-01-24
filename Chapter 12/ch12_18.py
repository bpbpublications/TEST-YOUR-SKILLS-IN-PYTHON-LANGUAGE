class Student:
    _school = 'Life School'
    count=0
    def __init__(self, name, standard):
        self.name=name 
        self.std=standard 
        Student.count+=1
        
class UGStudent(Student):
    def __init__(self, name, standard,age):
        super().__init__(name, standard)
        self.age=age
        

s1 = Student("Steve", 7)
print("Count:", s1.count)
s2= UGStudent("Smith", 7, 22)
print("Count:", s2.count)

