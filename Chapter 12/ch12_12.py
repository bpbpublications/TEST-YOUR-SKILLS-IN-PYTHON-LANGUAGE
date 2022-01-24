class Book:
    def get(self):
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")
        self.price=float (input("Enter price: "))
    def displayBook(self):
        print("Title:", self.title,", Author: ", self.author)
        print("Price: ", self.price)

class Novel(Book):
    def getInfo(self):
        super().get()
        self.genre = input("Enter genre: ")
    def displayNovel(self):
        super().displayBook()
        print("Genre= ", self.genre)

x1 = Book()
x1.get()
y1 = Novel()
y1.getInfo()
x1.displayBook()
y1.displayNovel()
