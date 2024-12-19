import numpy as np
iris_data=np.genfromtxt("./input/iris.csv",skip_header=1,dtype=float,delimiter=",",usecols=[0,1,2,3])
iris_data[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print(iris_data[np.sum(np.isnan(iris_data),axis=1)==0])
