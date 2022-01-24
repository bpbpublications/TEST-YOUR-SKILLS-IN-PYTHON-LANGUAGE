import math
list1 = [2,3,7]
cubed = list(map((lambda x: pow(x,3)), list1))
print(cubed)

# please note list() to be used before map to print elements as list