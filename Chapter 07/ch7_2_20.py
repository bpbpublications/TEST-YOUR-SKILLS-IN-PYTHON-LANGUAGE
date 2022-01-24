import math
list1 = [20,13,42,6]
list2 = filter(lambda x: x%3==0, list1)
print(list(list2))