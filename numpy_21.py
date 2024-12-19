# Question: Print or show only 3 decimal places of the numpy array rand_arr.
# Input: rand_arr = np.random.random((5,3))
import  numpy as np
a=np.random.uniform(5,10,size=(5,3))
print(a)
np.set_printoptions(precision=3)
print(a)
