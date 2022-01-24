import numpy as np
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2], [3, 4]])
comparison = a1 == a2
equal_arrays = comparison.all()
print(equal_arrays)

# True