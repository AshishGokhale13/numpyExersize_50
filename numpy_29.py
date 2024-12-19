# Question: Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 so that the minimum has value 0 and maximum has value 1.
import numpy as np
iris_data=np.genfromtxt("./input/iris.csv",skip_header=1,usecols=1,delimiter=",")
print((iris_data-np.min(iris_data))/(np.max(iris_data)-np.min(iris_data)))