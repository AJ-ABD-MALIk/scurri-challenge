'''
Created on Apr 21, 2021

@author: sogunfowora
'''

import numpy as np


def rename_multiples(arr):
    '''
    Rename multiples of 3, 5 and 15 in array provided
    :param arr: (array)

    :returns arr: (array)
    '''
    
    # Get indices for multiples of 3
    indices_mod_3 = np.where(arr % 3 == 0)
    
    # Get indices for multiples of 5
    indices_mod_5 = np.where(arr % 5 == 0)
    
    # Get indices for multiples of 15 using common indices from multiples of 3 and 5
    mod_indices_intersect = np.intersect1d(indices_mod_3, indices_mod_5)
    
    # Rename elements in the array
    arr[indices_mod_3] = 'Three'
    arr[indices_mod_5] = 'Five'
    arr[mod_indices_intersect] = 'ThreeFive'
    
    return arr


if __name__ == '__main__':
    arr = np.arange(1, 101, dtype="object")
    result = rename_multiples(arr)
    print(result)
