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
    def __init__(self, s1, s2):
        super().__init__(s1, s2, s1, s2)
        
r1=Rectangle(3, 7)
r1.perimeter()
