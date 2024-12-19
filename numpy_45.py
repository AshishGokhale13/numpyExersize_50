import numpy as np
dataset=np.genfromtxt("./input/diabetes.csv",delimiter=",",skip_header=1,usecols=[0,1,2,3,4],dtype=float)
c,v=np.unique(dataset[1:],return_counts=2)
print(v[np.argmax(c)])