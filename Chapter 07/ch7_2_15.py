def f15(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, ' is a leap year')
            else:
                print(year, ' is not a leap year')
        else:
            print(year, ' is a leap year')
    else:
        print(year, ' is not a leap year')

f15(400)
f15(1981)