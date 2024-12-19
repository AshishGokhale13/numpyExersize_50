import numpy as np
dataset=np.genfromtxt("./input/red_wine.csv",delimiter=",",skip_header=1,usecols=[0,1,2,3,4],dtype=float)

dataset[np.random.randint(150,size=20),np.random.randint(4,size=20)]=np.nan
print(np.isnan(dataset).any())