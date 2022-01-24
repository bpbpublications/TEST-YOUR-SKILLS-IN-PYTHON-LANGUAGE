class GovtEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def displayEmp(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
    
elist=[]
for i in range(3):
    n=input("Enter name of an employee: ")
    s=int(input("Enter salary of an employee: "))
    e=GovtEmployee(n,s)
    elist.append(e)

for e in elist:
    e.displayEmp()






