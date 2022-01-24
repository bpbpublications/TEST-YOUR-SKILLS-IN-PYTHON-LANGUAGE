def f11(n):
    if n == 2:
        print(n, ' is a prime number')
    elif n%2 == 0:
        print(n, ' is not a prime number')
    else:
        for i in range(3, int(n/2) , 2):
            if n % i == 0:
                print(n, 'is not a prime number')
                break
        if(i==n):
            print(n, ' is a prime number')

f11(29)