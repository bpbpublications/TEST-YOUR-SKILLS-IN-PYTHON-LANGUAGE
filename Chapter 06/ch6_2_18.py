fullname = "Aradhana Goyal"
for index in range(0, len(fullname)):
    if fullname[index] == ' ':
        space = index
        break
lastname = fullname[space:]
print("Last name is %s." % lastname)

# Last name is Goyal 