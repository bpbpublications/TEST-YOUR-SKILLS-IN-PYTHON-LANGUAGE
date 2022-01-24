def f9(n,x): 
    i=2 
    j=2 
    t=1 
    sum = 0   
    while t<=n:
        sum = sum + x**i * (-1)**j 
        print(sum)
        i= i+2
        j= j+1
        t = t+1
print(sum)

f9(3,2)