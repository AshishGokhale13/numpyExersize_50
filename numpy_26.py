# Question: Extract the text column species from the 1D iris imported in previous question.
import numpy as np
a=np.genfromtxt("./input/iris.csv",skip_header=1,usecols=[-1],delimiter=",",dtype=object)
print(a)