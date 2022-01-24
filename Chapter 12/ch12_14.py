class Quad:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)

class Polygon(Quad):
    def __init__(self, s1, s2, s3, s4):
        super().__init__(s1, s2, s3, s4)

p1=Polygon(3, 7, 5, 2)
p1.perimeter()
