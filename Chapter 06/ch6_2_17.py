fullname = "Prakriti Garg "
for index in range(0, len(fullname)):
    if fullname[index] == ' ':
        space = index
        break
firstname = fullname[0:space]
print("First name is %s." % firstname)

# First name is Prakriti 