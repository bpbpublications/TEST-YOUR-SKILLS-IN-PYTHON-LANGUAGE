y=2010
if y%4==0:
    if y%100==0:
        if y%400==0:
            print(y, ' is leap year')
        else:
            print(y, ' is not a leap year')
    print(y, ' is leap year')
else:
    print(y, ' is not a leap year')
