# Question: Convert the 1D iris to 2D array iris_2d by omitting the species text field.
import numpy as np
a=np.genfromtxt("./input/iris.csv",delimiter=",",skip_header=1,usecols=[0,1,2,3],dtype=float)
print(a)