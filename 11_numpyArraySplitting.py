# by using function array_split()

# split the array into three part 

import numpy as np 
x = np.array([1,2,3,4,5,6])
x_new = np.array_split(x,3)
print(x_new)

# output:-[array([1, 2]), array([3, 4]), array([5, 6])]

# ---------- now we will split this array in 4 parts

import numpy as np 
x = np.array([1,2,3,4,5,6])
x_new = np.array_split(x,4)
print(x_new)

# output:-[array([1, 2]), array([3, 4]), array([5]), array([6])]


# ------split into array

import numpy as np 
x = np.array([1,2,3,4,5,6])
x_new = np.array_split(x,3)
print(x_new[0])
print(x_new[1])
print(x_new[2])

# output :-
# [1 2]
# [3 4]
# [5 6]


# splitting the 2d array

import numpy as np
x = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
new_x = np.array_split(x,3)
print(new_x)

# output
# [array([[1, 2],[3, 4]]), array([[5, 6],[7, 8]]), array([[ 9, 10],[11, 12]])]


# ------split the 2-D array into three 2-D array

import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
new_x = np.array_split(x,3)
print(new_x)

# output :-
# [array([[1, 2, 3],[4, 5, 6]]), array([[ 7,  8,  9],[10, 11, 12]]), array([[13, 14, 15],[16, 17, 18]])]

# splitting the 2-D into three 3-D wit row
import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
new_x = np.array_split(x,3,axis=1)
print(new_x)

# output :-
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[ 2],
#        [ 5],
#        [ 8],
#        [11],
#        [14],
#        [17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]



# ---alternate solution is using the hsplit(),opposite hstack()
import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
new_x = np.hsplit(x,3)
print(new_x)

# output :-
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[ 2],
#        [ 5],
#        [ 8],
#        [11],
#        [14],
#        [17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]
