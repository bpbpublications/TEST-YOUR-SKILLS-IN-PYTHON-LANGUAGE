def f5(a,b):       
    while b:
        a,b = b, a%b 
        print (a)

f5(300,500)