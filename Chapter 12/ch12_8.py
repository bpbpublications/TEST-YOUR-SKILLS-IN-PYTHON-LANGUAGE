class Kid:
    kidsCount = 0
    def __init__(self, name, house):
        self.name = name
        self.house = house
        Kid.kidsCount += 1
    def displayCount(self):
        print( "Total Kids: ", Kid.kidsCount)
    def displayKid(self):
        print ("Name : ", self.name, ", House: ", self.house)

k1=Kid("Ayushi", "Air")
k1.displayKid()
k1.displayCount()
n=input("Enter name of a kid: ")
h=input("Enter house of a kid: " )
k=Kid(n,h)
k.displayKid()
k.displayCount()
