list1 = [5,50,'Five Hundred']
list2 = list(list1)
list2[2:3] = [500, 5000]
print(list2)


#[5,50,500,5000]