# Create 3D-numpy array of 2 rows and 2 columns
arr1 = np.arange(3 * 2 * 2).reshape(3, 2, 2)
  
print("Original 3D array:\n", arr1)
# Create 2D diagonal array
diag_arr1 = np.diagonal(arr1, axis1 = 1, axis2 = 2)
print("2D diagonal array:\n", diag_arr1)

#[[[0 1]
#[2 3]]
#[[4 5]
#[6 7]]
#[[8 9]
#[10 11]]]

#[[0 3]
#[4 7]
#[8 11]]

