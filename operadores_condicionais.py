# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:56:53 2021

@author: odp107589
"""

if 5 > 3:
    print('5 é maior que 3')
    
if 5 > 4:
    print('5 é maior')
else:
    print('5 não é maior')
    
n = 5
if n == 4:
    print('n é igual a 4')
else:
    if n == 3:
        print('n é igual a 3')
    else:
        print('n não é igual a 4 nem a 3')        
        
x = 1
y = 5
if (x > 1) or (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('uma ou nenhuma das condições foram satisfeitas')