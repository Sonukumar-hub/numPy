# array indexing is the same as accessing an array

# start with 1D array

import numpy as np
x = np.array([1,2,3,4])

print(x[0])


# we can get the third and fourth element from adding them
import numpy as np
x = np.array([1,2,3,4])

print(x[2]+x[3])

# acessing the 2d  

import numpy as np
x = np.array([[1,2,3,4],[5,6,7,8]])

print(x[0,2])


# acessing 3D array
x = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])
import numpy as np

x = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])

print(x[0,1,2])

