# creating a hdf5 file sample.

import numpy as np
from h5py import File as hdf_file

# storing a simple 3x3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with hdf_file('hdf5_data_sample1.h5', 'w') as hdf:
    hdf.create_dataset('matrix', data=matrix)

# creating random matrix using numpy
matrix_1 = np.random.random(size=(1000, 1000))      # a 1000 x 1000 matrix
matrix_2 = np.random.random(size=(10000, 10000))  # a 100000 x 100000 matrix
with hdf_file('hdf5_data_sample2.h5', 'w') as hdf:
    hdf.create_dataset('matrix_1', data=matrix_1)
    hdf.create_dataset('matrix_2', data=matrix_2)
