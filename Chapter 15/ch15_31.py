import numpy as np
arr1 = np.array([1, 2, 3,4,5,5,5])
print(np.bincount(arr1).argmax())

#5