lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

lastNumber = 6
for row in range(lastNumber,0,-1):
    for column in range(row-1, 0,-1):
        print(column, end=' ')
    print("")

'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
'''