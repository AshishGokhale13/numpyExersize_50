# Extract a element from 1D array which statisfy the condition
# Etract odd numbers from numpy

import numpy as np
array=np.arange(11)

# by fancy indexing printing the only odd Number position
print(array%2==1)

#Extracting the odd number which are present in givent array
print(array[array%2==0])

# How to replace items that satisfy a condition with another value in numpy array