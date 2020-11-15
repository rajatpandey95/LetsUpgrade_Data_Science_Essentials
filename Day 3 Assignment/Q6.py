import numpy as np

number_list = np.array([1,1,1,2,2,2,5,25,1,1])
(unique, counts) = np.unique(number_list, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)
