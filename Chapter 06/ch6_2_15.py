name = input("Enter your name: ")
while not name.isalpha():
    print("That is not a valid name.")
    name = input("Enter your name: ")
print(name)

#asks ur to enter name till it contains all alphabets