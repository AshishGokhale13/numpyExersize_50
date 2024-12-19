# Question: Insert np.nan values at 20 random positions in iris_2d dataset
import numpy as np
iris_data=np.genfromtxt("./input/iris.csv",delimiter=",",skip_header=1,dtype=float,usecols=[1,2,3,4])
for i in np.random.randint(0,len(iris_data),20):
    iris_data[i]=np.nan
print(iris_data)

