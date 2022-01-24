num=0
count=0
sum=0
while num>=0:
    num = int(input('enter any number .. -1 to exit: '))
    if num >= 0:
        count = count + 1         
    sum = sum + num 
avg = sum/count
print('Total numbers:', count, ', Average: ', avg)

''' output
1
2
-1
Total numbers:2,  Average:1.0