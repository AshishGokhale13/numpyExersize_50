import numpy as np
iris_data = np.genfromtxt('./input/iris.csv', delimiter=',', 
                          dtype=object, usecols=[1,2,3,4], skip_header=1)

np.random.seed(100)
a = np.array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
species_out = np.random.choice(a, 150, p=[0.5, 0.25, 0.25])
print(np.unique(species_out, return_counts=True))