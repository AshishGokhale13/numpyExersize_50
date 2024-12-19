# Replace the element without affecting the original array
import numpy as np
a=np.array([1,2,3,4,5])
b=np.copy(a)
b[b%2==1]=-1
print(b)
print(a)



