import numpy as np
  
# Create 3D-numpy array of 2 rows and 2 columns
arr3 = np.arange(3 * 2 * 3).reshape(3, 2, 3)
  
print("Original 3D array:\n", arr3)

#  [[[0 1 2]
#[3 4 5]]
#[[6 7 8]
#[9 10 11]]
#[[12 13 14]
[15 16 17]]]

# Create 2D diagonal array
diag_arr3 = np.diagonal(arr3, axis1 = 1, axis2 = 2)
  
print("2D diagonal array:\n", diag_arr3)

#[[0 4]
#[6 10]
#[12 16]]