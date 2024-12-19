import numpy as np
np.set_printoptions(precision=2)
np.random.seed(100)
a=np.random.uniform(1,70,100)
a[a<10]=10
a[a>30]=30
np.set_printoptions(threshold=2)
print(a)