# Example for create an boolean array
import numpy as np

# print and 3X3 array using full method which have only true values
array=np.full((3,3),True,dtype=bool)
print(array)

# created first 1D array with having true value and then using reshape method converted it into 3X3 Array
array=np.full(9,True,dtype=bool).reshape(3,3)
print(array)


# np.ones method is used to return true value as 1 or boolead true value only
array=np.ones((3,3),dtype=bool)
print(array)

array=np.ones(9,dtype=bool).reshape(3,3)
print(array)
