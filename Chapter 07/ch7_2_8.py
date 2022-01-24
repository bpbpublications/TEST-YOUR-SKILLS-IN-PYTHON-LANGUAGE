def f8(n): 
    m = n   
    sum = 0 
    while m!=0:
        x = m%10
        sum = sum + x**3
        m = m//10
        if sum == n:
            print(n, " is an Armstrong number")
        else:
            print(n, " is not an Armstrong number")

f8(153)
f8(125)