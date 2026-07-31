# Now we will create a numpy ndArray object
# the array object in numpy is called ndarray

# using list
import numpy as np

x=np.array([1,2,3,4,5])
print(x)
print(type(x))


# using tuple
import numpy as np

x=np.array((1,2,3,4,5)) 
print(x)
print(type(x))


# Dimensions in Array - a dimension in arrays is one level of array depth(nested array)

# 0-D array - scalars,are the elements in an array,each value in an array is a 0-D array

# Now we will create 0_d array with value 42

import numpy as np

x=np.array(42)
print(x)
print(type(x))


# 1-D array- is an array that has 0-D arrays as its element is called 1D array or uni directional

import numpy as np

x=np.array([1,2,3,4,5])
print(x)
print(type(x))

# create a 2d arraycontaining 2 Array with certain values.

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
print(x)
print(type(x))

# create 3D array with 2-D array

import numpy as np

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x)
print(type(x))

# check how many dimension the array have: ndim attribute

import numpy as np

x=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(x.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# create a 1D array and convert it to  5 dimension array and verify that it has 5 dimension
import numpy as np
shared = np.array([1,2,3,4,5],ndmin=5)
print(shared)
print('number of dimension ', shared.ndim)