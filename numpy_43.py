# Question: What is the value of second longest petallength of species setosa
# For this question I am going to find second highest bloodpressure (2nd column) where outcome is 1
import numpy as np
dataset=np.genfromtxt("./input/diabetes.csv",skip_header=1,usecols=[0,1,2,3,4],dtype=float,delimiter=",")

bloodpressure=dataset[dataset[:,2]>80,[2]].astype(float)
print(np.unique(np.sort(bloodpressure))[-2])