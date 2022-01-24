class PGStudent:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def displayS(self):
        print ("Name : ", self.name, ", Marks: ", self.marks)
slist=[]
for i in range(3):
    n=input("Enter name of the student: ")
    m=int(input("Enter marks of the student: "))
    s=PGStudent(n,m)
    slist.append(s)
max=-1
s1= ""
for s in slist:
    s.displayS()

    if s.marks>max:
        max=s.marks
        s1=s.name

print("Student with max marks:", s1)
