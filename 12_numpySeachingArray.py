# searching array :- you can search an array for a certain value and return the index that get the match by using where()

import numpy as np

x = np.array([1,2,3,4,5,4,4])
x_new = np.where(x == 4)
print(x_new)

# output :-- (array([3, 5, 6]))



#------- now we will find the indexes where the value are even

import numpy as np

x = np.array([1,2,3,4,5,4,4])
x_new = np.where(x%2 == 0)
print(x_new)

# output :- (array([1, 3, 5, 6]),)


# ------------------searchorted():-perform binary search and give index-------------

import numpy as np

x = np.array([6,7,8,9])
x_new = np.searchsorted(x,7)
print(x_new)

# output:-1


import numpy as np

x = np.array([6,7,8,9])
x_new = np.searchsorted(x,(7,8))
print(x_new)

# output :- [1,2]


# ----now we will search from right search


import numpy as np

x = np.array([6,7,8,9])
x_new = np.searchsorted(x,7,side='right')
print(x_new)

# output:-2


# how to insert in array using binary search it will give index


import numpy as np

x = np.array([6,7,9])
x_new = np.searchsorted(x,[1,2,8,10,11])
print(x_new)



