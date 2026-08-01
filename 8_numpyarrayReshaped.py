# reshaping - means changing the shape of an array, like adding or removing the element

# reshaping from 1-D to 2-D

import numpy as np 
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = x.reshape(4,3)
print(y)

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]



# reshaping from 1D to 3d
z = x.reshape(2,3,2)
print(z)

# output - [[[ 1  2]
            #   [ 3  4]
            #   [ 5  6]]

            #  [[ 7  8]
            #   [ 9 10]
            #   [11 12]]]
