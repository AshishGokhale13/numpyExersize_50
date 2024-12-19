import numpy as np
def counts_of_all_values_rowwise(arr2d):
    # Unique values and its counts row wise
    num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]

    # Counts of all values row wise
    return([[int(b[a==i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array])

np.random.seed(100)
np.set_printoptions(threshold=10)
arr = np.random.randint(1,11,size=(6, 10))
arr
print(np.arange(1,11))
print(counts_of_all_values_rowwise(arr))