import numpy as np
# 2d array with 5 rows 2 columns
a=np.arange(1,11).reshape(5,2)
print(a)
# 2d array with 5 rows 2 columns
b=np.arange(11,21).reshape(5,2)
print(b)
# combining two array vertically in single 2d array wich is one column
print(np.vstack((a,b)))