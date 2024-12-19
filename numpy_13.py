# Question: Get the positions where elements of a and b match
import numpy as np
a=np.array([1,2,3,5,4,3,2])
b=np.array([4,5,3,6,4,1,2])

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 0, 3], [0, 5, 9]])

print(np.where(a==b))