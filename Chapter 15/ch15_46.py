import numpy as np
n_array = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
  
diag = np.diagonal(n_array)
print("Diagonal elements:", end= '')
print(diag)
#[1 5 9]

print("Sum of diagonal elements:" , end= '')
print(sum(diag))

#15