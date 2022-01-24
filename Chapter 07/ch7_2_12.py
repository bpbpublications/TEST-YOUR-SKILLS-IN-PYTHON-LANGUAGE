def f12(n): 
    sum = 0 
    while n != 0:
        k = n % 10
        sum = sum + k
        k = int(n / 10)
        n = k
    print("Sum of digits: ", sum)

f12(123)