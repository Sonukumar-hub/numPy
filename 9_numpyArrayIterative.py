# iterative array - means going through the element one by one or step by step. like for loop

# iterate element of 1-D
import numpy as np 
x = np.array([1,2,3,4])

for i in x:
    print(i)



# iterate in 2d array

import numpy as np 
y = np.array([[1,2,3,4],[5,6,7,8]])

for i in y:
    for a in i:
        print(a)




# iterate in 3d array

import numpy as np 
y = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

for i in y:
    for a in i:
        for b in a:
            print(b)



# Iterating the array with nditer() function

import numpy as np;
x = np.array([[[1,2],[3,4],[5,6]]])

for i in np.nditer(x):
    print(i)


# Now we will iterate with different step size

import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(x[:,::2]):
    print(i)