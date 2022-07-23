# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:48:52 2021

@author: odp107589
"""

a = 'casaco';

maiuscula = a.upper();

print(a)
print(maiuscula);

capital = a.capitalize()
print(capital)

metade_palavra = a[0:3]
print(metade_palavra)

ultimas_letras = a[3:]
print(ultimas_letras)

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('o', 'a')
print(a)
print(c)

print(c.find('s'))
print(c.find('k'))

e = ' casaco '
print(len(e))

f = e.strip()
print(f)
print(len(f))

n1 = 14
n2 = 16
print('Dividindo {n1} por {n2} o resultado é {n1/n2}')
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')