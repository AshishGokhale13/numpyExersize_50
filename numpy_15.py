#  How to make a python function that handles scalars to work on numpy arrays?
import numpy as np

def maxx(x,y):
    if(x>y):return x
    return y
def pairmax(x,y):
    maximum=[maxx(a,b) for a,b in map(lambda a,b:(a,b),x,y)]
    return np.array(maximum)

a=np.array([1,4,3646,464,5342346,425,32432,532,36326,23])
b=np.array([3,435,35,5353,535,5235,2352,5235,5,3523])
print(pairmax(a,b))