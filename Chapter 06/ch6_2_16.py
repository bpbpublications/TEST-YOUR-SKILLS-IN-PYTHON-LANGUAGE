marks = input("Enter your marks: ")
while not marks.isdigit():
    print("Marks invalid. Input again:")
    marks = input()

# asks user to enter marks till it contains all digits