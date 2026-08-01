#shape of an array - the shape of an array is the number of elements in each directions
# now we will try to get the shape of any array


import numpy as np

x = np.array([[1,2,3],[4,5,6]])
print(x.shape)

# output - (2,3) which means the array has 2 dimension and it has 3 element



arr = np.array([10, 20, 30, 40])
print(arr.shape)



# --------------------------------------

arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(arr.shape)

# output = (2, 2, 2)    
# 2 groups
# 3 rows in each group
# 4 columns in each row


y = np.array([1,2,3,4],ndmin=5)
print(y)
print(y.shape)

# [[[[[1 2 3 4]]]]]
# (1, 1, 1, 1, 4)