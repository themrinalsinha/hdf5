# Reading Groups in HDF5 Files

import numpy as np
import h5py

with h5py.File('hdf5_groups.h5', 'r') as hdf:
    base_items = list(hdf.items())
    print(f'Items in base directory: {base_items}')

    # Get Group 1
    G1 = hdf.get('Group_1')
    print(f'\nItems in Group_1: {G1.items()}')

    dataset_4 = np.array(G1.get('dataset_4'))
    print(dataset_4.shape)

    # Get Group 2
    G2 = hdf.get('Group_2')
    print(f'\nItems in Group_2: {G2.keys()}')
    G2_SUB_G_1 = G2.get('SubGroup_1')
    print(G2_SUB_G_1.get('dataset_3'))
