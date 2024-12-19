# find the correlation of two columns
import numpy as np
dataset =np.genfromtxt("./input/diabetes.csv",delimiter=",",skip_header=1,usecols=[1,2,3,4],dtype=float)
print(np.corrcoef(dataset[:1],dataset[:5]))
