# Replace a value as -1 where odd numbers are present in array
import numpy as np 
# Geratign the 1D array using arange method 
array=np.arange(1,11)

# by using fancy indexing replacing the odd number by -1
array[array%2==1]=-1

print(array)
