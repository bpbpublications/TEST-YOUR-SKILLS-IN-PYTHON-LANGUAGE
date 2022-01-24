i = 2
while(i < 20):
   j = 2
   while(j <= (i/j)):
      if not(i%j): 
        break
      j = j + 1
   if (j > i/j) : 
       print (i, end=" ")
   i = i + 1


# 2 3 5 7 11 13 15 17 19 

