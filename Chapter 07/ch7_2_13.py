def f13(): 
    k = 1 
    sum = 0 
    multi = 1

    print("Enter a number: ") 
    n = int(input())
    print("Enter the number of digits: ") 
    nd = int(input()) 
    while k <= nd:

        k1 = n % 10 
        print(k1)
        sum = sum + k1 
        n = int(n / 10) 
        k = k + 1
    print("Sum of digits: ", sum)

f13()