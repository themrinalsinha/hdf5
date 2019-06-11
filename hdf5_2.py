# Reading HDF5 files

import numpy as np
from h5py import File as hdf_file

with hdf_file('hdf5_data_sample1.h5', 'r') as hdf:
    print(f'List of keys of datasets in file: {hdf.keys()}')
    print(f'Value of key: {hdf.get("matrix")}')
    print(f'Actual value: {hdf.get("matrix")[()]}') # new way of getting dataset .value is deprecated
    print(f'Name of dataset: {hdf.get("matrix").name}')

    # Converting value directly to numpy array
    dataset = np.array(hdf.get('matrix'))
    print('\ngetting value via. numpy \n', dataset)
    print(f'Shape of the matrix is: {dataset.shape}')

print('===============================================================')

with hdf_file('hdf5_data_sample2.h5', 'r') as hdf:
    print(f'List of keys of datasets in file: {hdf.keys()}')
    print(f'Value of key: {hdf.get("matrix_1")}')
    print(f'Actual value: {hdf.get("matrix_1")[()]}') # new way of getting dataset .value is deprecated
    print(f'Name of dataset: {hdf.get("matrix_1").name}')

    # Converting value directly to numpy array
    dataset = np.array(hdf.get('matrix_1'))
    print('\ngetting value via. numpy \n', dataset)
    print(f'Shape of the matrix is: {dataset.shape}')

