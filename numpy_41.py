import numpy as np
dataset=np.genfromtxt("./input/red_wine.csv",skip_header=1,usecols=[0,1,2,3,4,11],dtype=float,delimiter=",")
bins=np.array([0,3,5,7])
labal={1:11,2:22,3:33,4:44}
catogorical_data_inds=np.digitize(dataset[:,5].astype(float),bins)
catagory_data=[labal[x] for x in catogorical_data_inds]
category_data = np.array([11, 22, 33, 11])[:, np.newaxis]
print(np.hstack([dataset,catagory_data]))
