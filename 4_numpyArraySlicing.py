# slicing array -slicing in python means taking element from one give index toanother index;
# [start:end],[start,end,stop]

# now we will slice an element from 1 to 5

import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[0:5])

# now we will slinve from index4 to the end value
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[4:])

# now we will slice the element from the begining
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[:5])

# negative slicing

import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[-6:-1])


# steps: you will use step value to determine the step of the slicing
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[1:5:2])


# now return every array number from the entire array
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x[::2])

# slicing 2D array
import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[1,1:4])

# another example 
import numpy as np
x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[0:2,2])

# another example tought print fro both index 1:4
import numpy as np
x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[0:2,1:4])
