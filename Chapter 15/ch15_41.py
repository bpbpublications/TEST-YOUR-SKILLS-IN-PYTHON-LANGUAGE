import numpy as np
matrix= np.arange(1,9).reshape((3, 3))
print(matrix)
print(matrix.shape)

#Value error canno reshape array of size 8 into shape(3,3)