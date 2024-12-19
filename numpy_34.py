# How to filter numpy array with two more conditions
import numpy as np
iris_Data=np.genfromtxt("./input/iris.csv",skip_header=1,delimiter=",",dtype=float,usecols=[0,1,2,3])

iris_Data_filtered=iris_Data[(iris_Data[:,2]>1.5)&(iris_Data[:,0]<5.0)]
print(iris_Data_filtered)


