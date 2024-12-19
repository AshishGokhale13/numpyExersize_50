# Question. Find the 5th and 95th percentile of iris's sepallength
import numpy as np
iris_Data=np.genfromtxt("./input/iris.csv",delimiter=",",usecols=[1],dtype=float,skip_header=1)
print(np.percentile(iris_Data,q=[5,95]))