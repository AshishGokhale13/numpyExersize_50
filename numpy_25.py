import numpy as np
# Question: Import the iris dataset keeping the text intact.

# Solution:
iris_data=np.genfromtxt("./input/iris.csv",delimiter=",",skip_header=1,usecols=[0,1,2,3],dtype=object)
print(iris_data)