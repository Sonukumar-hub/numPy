# getting some elements out of some existing array is called filtering

# A boolean index list is a list of boolean corresponding to indexing in the array .(true and false)


# creating filter array

import numpy as np
x = np.array([41,42,43,44])
emptyX = []

for element in x:
    if element > 42:
        emptyX.append(True)
    else:
        emptyX.append(False)

new_x = x[emptyX]
print(emptyX)
print(new_x)

# create a filter array that will return only even element from original array

import numpy as np
x = np.array([1,2,3,4,5,6,7])
emptyX = []

for i in x:
    if i%2 == 0:
        emptyX.append(True)
    else:
        emptyX.append(False)

new_X = x[emptyX]
print(new_X)