# Question: Find the mean, median, standard deviation of iris's sepallength (1st column)
import numpy as np
a=np.genfromtxt('./input/iris.csv',delimiter=",",usecols=1,skip_header=1)
print(f'mean of sepal_length { np.mean(a)}')
print(f'median of sepal_length { np.median(a)}')
print(f'standard deviation of sepal_length { np.std(a)}')