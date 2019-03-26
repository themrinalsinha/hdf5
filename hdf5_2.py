# Reading from HDF5 files.

import numpy as np
import h5py

with h5py.File('hdf5_data.h5', 'r') as hdf:
    print(f'List of datasets in file: {hdf.keys()}')
    dataset_1 = hdf.get('dataset1')
    dataset_2 = hdf.get('dataset2')

    print(np.array(dataset_1))
    print(np.array(dataset_2))

    print(f'Shape of dataset_1 is: {np.array(dataset_1).shape}')
    print(f'Shape of dataset_2 is: {np.array(dataset_2).shape}')
