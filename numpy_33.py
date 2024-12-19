# Question: Find the number and position of missing values in iris_2d's sepallength (1st column)

import numpy as np
iris_data=np.genfromtxt("./input/iris.csv",delimiter=",",skip_header=1,dtype=float,usecols=[1])
print(iris_data)
iris_data[np.random.randint(0,len(iris_data),20)]=np.nan
print(iris_data)
print(np.where(np.isnan(iris_data)))
