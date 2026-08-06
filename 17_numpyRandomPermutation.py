# Permutation refers to an arrangement of element like [3,2,1] is permutation of [1,2,3] and vice versa

# THe numpy random module provide two method : shuffle() and Permutation

# Now we will randomly suffle elements for the below array:

# In shuffle : it changes the original array

from numpy import random
import numpy as np

x = np.array([1,2,3,4,5,6])

random.shuffle(x)
print(x)


# output :- [2 4 1 6 5 3]


# now we will generate a permutation of element for the below array:

# permutation method(), leaves the original array unchange

from numpy import random
import numpy as np

y = np.array([1,2,3,4,5,6])

z = random.permutation(y) 
# it does not change original array
print(z)

# output - [3 5 4 2 6 1]
