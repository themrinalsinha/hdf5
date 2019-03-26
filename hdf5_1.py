import numpy as np
from h5py import File as hdf_file

matrix_1 = np.random.random(size=(1000, 1000))
matrix_2 = np.random.random(size=(100000, 1000))

with hdf_file('hdf5_data.h5', 'w') as hdf:
    hdf.create_dataset('dataset1', data=matrix_1)
    hdf.create_dataset('dataset2', data=matrix_2)
