# joining the numpy array- here for this we will pass concatenate()

import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

z = np.concatenate((x,y))

print(z)


# joining of 2D along with rows(axis = 1)


import numpy as np 

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

z = np.concatenate((x,y))

print(z)

# output 
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]



import numpy as np 

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

z = np.concatenate((x,y),axis=1)   

print(z)

# output 
# [[1 2 5 6]
#  [3 4 7 8]]



# joining array with stack function : 

import numpy as np 

x = np.array([1,2,3])
y = np.array([4,5,6])

z = np.stack((x,y),axis=1)

print(z)

# output
# [[1 4]
#  [2 5]
#  [3 6]]



# stacking along with rows:hstack()

import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])

z = np.hstack((x,y))

print(z)

# output : [1 2 3 4 5 6]



# note there are many method do it using documentation