import numpy as np
dataset=np.genfromtxt("./input/red_wine.csv",skip_header=1,usecols=[0,1,2,3,4],delimiter=",",dtype=float)
print(np.unique(dataset,return_counts=True))