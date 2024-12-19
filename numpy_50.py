import numpy as np
a=np.arange(1,20,0.2)
b=np.arange(21,30,0.5)
c=np.arange(31,20,0.7)

print(np.concatenate([a,b,c]))
