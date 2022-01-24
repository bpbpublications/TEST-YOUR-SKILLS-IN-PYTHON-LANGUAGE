def f14(n): 
    count = 0
    print('Numbers from 1 to n not divisible by 2,3 and 5') 
    for num in range(n+1):
        if num%2 != 0 and num%3!=0 and num%5!=0: 
            print( num)
            count = count + 1; 
    print('Total numbers: ', count )

f14(30)