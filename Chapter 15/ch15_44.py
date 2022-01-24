import numpy as np
n_arr = np.array([-75.4, 42.45, 60.0])
n_arr[n_arr < 0] = 0
print(n_arr)
a2=np.delete(n_arr,[0])
print(a2)

#[0. 42.45. 60.0]
#[42.45 60.0]