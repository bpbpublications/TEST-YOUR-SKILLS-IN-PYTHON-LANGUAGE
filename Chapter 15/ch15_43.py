import numpy as np
n_arr = np.array([75.42, 42.45, 60.0])
n_arr[n_arr > 50.] = 100.50
print(n_arr)

#[100.5 42.45 100.5]