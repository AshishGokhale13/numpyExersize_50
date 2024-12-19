import numpy as np
np.random.seed(100)
a=np.random.uniform(1,50,20)
sort=a.argsort()
print('postions')
print(sort[-5:][::-1])
print('values')
print(a[sort][-5:][::-1])
