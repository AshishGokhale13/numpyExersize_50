# Question: Print the full numpy array a without truncating.
# Input: np.set_printoptions(threshold=6)
# a = np.arange(15)
# a
import numpy as np
a=np.arange(15)
np.set_printoptions(threshold=15)
print(a)

