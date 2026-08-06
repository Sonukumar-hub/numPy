 # data distribution is a list of all possible value and how often each value occur
# such list are important when working with statistic and data science

# it's module are 
# 1. random distribution : probability function 

# now we will generate 1-D with 100 value where each value has to be 3,5,7,9

# the probabiliy for the value 3 is said to be 0.1

# the probabiliy for the value 5 is said to be 0.3

# the probabiliy for the value 7 is said to be 0.6

# the probabiliy for the value 9 is said to be 0

# the sum of all probability number shoul be 1; 

from numpy import random
x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))

print(x)

# now we will return 2D with 3 row each having 5 value

from numpy import random
x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))

print(x)