i=1
sum_e=0
sum_o=0 
while i<=5:
    n=int(input())
    if n%2==0:
        sum_e+=n
    else:
        sum_o+=n
    i=i+1
print("Sum of even numbers: ", sum_e)
print("Sum of odd numbers: ", sum_o)

''' output
1
2
3
4
5
Sum of even numbers:6
Sum of odd numbers: 9
'''

