import numpy as np
dataset=np.genfromtxt("./input/red_wine.csv", skip_header=1 ,  usecols=[0,1,2,3],delimiter=",",dtype=float)
dataset[np.random.randint(100,size=20),np.random.randint(4,size=20)]=np.nan
print(np.isnan(dataset).any())
dataset[np.isnan(dataset)]=0
print(dataset)
print(np.isnan(dataset).any())