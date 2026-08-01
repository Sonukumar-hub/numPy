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

# output -
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]


# unknown dimension - you are only allowed to have one unknown dimension . pass -1
# -1 represent how many no of element shold present in a row
shared = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
shared1 = shared.reshape(2,2,-1)

print (shared1)


# flatening the array by converting multidimensional array in 1-D

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(-1)
print(b)


# output - [1 2 3 4 5 6]

# there are alot of function for changing the shape of an arrayin numpy. like flatten,ravel and also rearranging the element rot90,flip,fliplr,flipud. they all are actually comes under advance numpy