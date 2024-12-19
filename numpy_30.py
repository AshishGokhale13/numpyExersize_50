# Question: Compute the softmax score of sepallength.
import numpy as np
iris_data=np.genfromtxt("./input/iris.csv",delimiter=",",usecols=[1],dtype=float,skip_header=1)
softmax=np.exp(iris_data)/sum(np.exp(iris_data))
print(softmax.sum())