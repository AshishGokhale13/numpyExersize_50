# Question: From array a remove all items present in array b
import numpy as np;
a=np.array([1,2,3,4,5])
b=np.array([1,5,6,7,4])
print(np.setdiff1d(a,b)) #inds the set difference of two arrays, returning the elements of a that are not present in b