import numpy as np
# 2d array with 4 rows 3 columns
a=np.arange(1,13).reshape(2,2,3)
print(a)
# 2d array with 4 rows 3 columns
b=np.arange(11,23).reshape(2,2,3)
print(b)
# combining the two 2d array in 4 row and 6 columns
print(np.hstack((a,b)))
