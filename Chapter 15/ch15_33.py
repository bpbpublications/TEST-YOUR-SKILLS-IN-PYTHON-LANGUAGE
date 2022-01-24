import numpy as np
arr1 = np.array([11, 12, 3,4,5])
freq=np.bincount(arr1)
maximum = max(freq)
for i in range(len(freq)):
    if freq[i] == maximum:
        print(i, end=" ")

# 3 4 5 11 12