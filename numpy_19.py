# Question: Reverse the columns of a 2D array arr.

# Input: arr = np.arange(9).reshape(3,3)

# Solution   
import numpy as np
a=np.arange(9).reshape(3,3)
print(a[:,::-1])