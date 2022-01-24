class Quad:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)

class Rectangle(Quad):
    def __init__(self, a,b):
        super().__init__(a, b, a, b)

    def area(self):
        a = self.side1 * self.side2
        print("area of rectangle=", a)
        
p1=Rectangle(5, 2)
p1.perimeter()
p1.area()
