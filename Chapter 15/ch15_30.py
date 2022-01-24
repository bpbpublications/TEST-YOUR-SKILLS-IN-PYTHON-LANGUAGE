import numpy
arr1 = numpy.array([[1, 2, 3],
                   [4, 5, 6],     
                   [7, 8, 9]])

print([1, 2, 3, 4] in arr1.tolist())
print([1, 2, 3] in arr1.tolist())

#False
#True