i=1
sum_e,sum_o=0,0 
while i<=10:
    if i%2==0: 
        sum_e+=i
    else:
        sum_o+=i
    i=i+1
print("Sum of even numbers: ", sum_e)
print("Sum of odd numbers: ", sum_o)

# Sum of even numbers: 30
# Sum of odd numbers: 25