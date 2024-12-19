#  Question: Get the common items between a and b
# Input: a=[1,2,3,2,3,4,3,4,5,6]
#        b =[7,2,10,2,7,4,9,4,9,8]
# Output: array([2, 4])
import numpy as np
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b)) # finds the intersection of two arrays, returning the sorted, unique values that are common to both.
