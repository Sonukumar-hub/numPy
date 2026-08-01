#data types in python: String,integer,float,boolean,complex
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode dtring
# v -memory

# chacking the data type of numpy array - dtype

import numpy as np
x = np.array([1,2,3,4,5])
print(x.dtype)

# checking the data type of numpy array - string

import numpy as np
x = np.array(['apple','mango','banana'])
print(x.dtype)


# creating array with a defined data type
import numpy as np
x = np.array([1,2,3,4,5],dtype='S')
print(x)
print(x.dtype)


# now we will create an array with data type of 4 byte int:
import numpy as np
x = np.array([1,2,3,4,5],dtype='i4')
print(x)
print(x.dtype)


# if a type is given in which the element cannot be casted then numpy will raise error. what if a value can not be converted

# import numpy as np
# x = np.array(['a','2','3'], dtype='i')
# print(x)
# print(x.dtype)


# converting data type in existing array- astype()

import numpy as np
x = np.array(['1','2','3'])
x1=x.astype('i')
print(x1)
print(x1.dtype)


# converting data type from integer to boolean

import numpy as np
x = np.array([1,0,3],)
x1=x.astype(bool)
print(x1)
print(x1.dtype)