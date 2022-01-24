x = False
y = False
z = False
if x or y:
    print (1)
elif not x and (not y and z):
    print (2)
elif (not x or y) or (y and x):
    print (3)
else:
    print (4)