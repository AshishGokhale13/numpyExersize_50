import numpy as np
dataset=np.genfromtxt("./input/red_wine.csv",delimiter=",",skip_header=1,usecols=[4],dtype=object)
print(np.argmax(dataset[:].astype(float)<1))