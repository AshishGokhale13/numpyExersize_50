# Question: Limit the number of items printed in python numpy array a to a maximum of 6 elements.
import numpy as np
a=np.arange(15)
np.set_printoptions(threshold=2)
print(a)
