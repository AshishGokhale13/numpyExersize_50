import numpy as np
dataset=np.genfromtxt("./input/iris.csv",skip_header=1,usecols=[2],dtype=float,delimiter=",")
bins=np.array([0,3,5,7])
inds=np.digitize(dataset.astype(float),bins)
label={1:"small",2:"medium",3:"Large"}
iris_categorical_Data=[label[x] for x in inds]
print(iris_categorical_Data)