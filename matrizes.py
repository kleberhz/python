# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:15:37 2021

@author: odp107589
"""

import numpy as np

matriz = np.array([[2, 3, 1], [4, 5, 7]])

print(matriz)
print(matriz.shape)
print(matriz[0])

print(matriz[0][1])

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])