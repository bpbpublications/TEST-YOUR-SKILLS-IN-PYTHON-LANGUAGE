class Point3D:
    counter=0
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
        Point3D.counter+=1
    def displayPoint3D(self):
        print("x= ",self.x, "y= ", self.y, "z=", self.z)
    def countPoints(self):
        print(Point3D.counter)
p1=Point3D(12,10,10)
p1.displayPoint3D()
p2=Point3D(2,10,20)
p2.displayPoint3D()
p1.countPoints()
p2.countPoints()
