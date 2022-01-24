def myFun(x):
    print("Value received:", x, "id:", id(x))
 
x = 13
print("Value passed:", x, "id:", id(x))
myFun(x)
