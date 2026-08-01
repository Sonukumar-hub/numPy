#difference between numpy array copy and view 

# copy---------
import numpy as np

arr = np.array([1, 2, 3, 4])

x = arr.copy()

x[0] = 100

print(arr)   # [1 2 3 4]
print(x)     # [100   2   3   4]


#view----------

import numpy as np

arr = np.array([1, 2, 3, 4])

x = arr.view()

x[0] = 100

print(arr)   # [100   2   3   4]
print(x)     # [100   2   3   4]