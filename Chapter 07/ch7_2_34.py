t=50
def add(x, y):
    global t
    t=x+y
    print ("in add() total=",t)
add(10,20)
print ("global variable, t=",t)