# Random meaning - something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100

from numpy import random
x = random.randint(100)
print(x)

# you can also genrate float() via rand from 0 to 1
from numpy import random
x = random.rand(3)
print(x)

# you can also generate random array
# we will generate a 1d array containing 5 random array
from numpy import random
x = random.randint(100,size=(5))
print(x)


# we will generate a 2d array with 3 rows, each row contains 5 random int from 0 to 100

from numpy import random
x = random.randint(100,size=(3,5))
print(x)


# you can also generate random number from an array - using choice()

from numpy import random
x = random.choice([3,5,7,9,1,4,6])
print(x)


# create 2d array using element of 1d array of random number
# we will generate a 1d array containing 5 random array
from numpy import random
x = random.choice([3,5,6,7,3,6,7],size=(3,5))
print(x)