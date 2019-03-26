# Creating Groups and Subgroups

import numpy as np
import h5py

matrix_0  = np.random.random(size=(1000, 1000))
matrix_1 = np.random.random(size=(1000, 1000))
matrix_2 = np.random.random(size=(1000, 1000))
matrix_3 = np.random.random(size=(1000, 1000))
matrix_4 = np.random.random(size=(1000, 1000))

with h5py.File('hdf5_groups.h5', 'w') as hdf:
    # Group 1 with two datasets
    G1 = hdf.create_group('Group_1')
    G1.create_dataset('dataset_1', data=matrix_1)
    G1.create_dataset('dataset_4', data=matrix_4)

    G2   = hdf.create_group('Group_2')
    G2.create_dataset('dataset_0', data=matrix_0)
    G2_1 = hdf.create_group('Group_2/SubGroup_1')
    G2_1.create_dataset('dataset_3', data=matrix_3)
    G2_2 = hdf.create_group('Group_2/SubGroup_2')
    G2_2.create_dataset('dataset_2', data=matrix_2)
