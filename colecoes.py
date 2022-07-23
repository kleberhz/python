# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:58:29 2021

@author: odp107589
"""

tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla)
print(tupla[0])

print(tupla.index('Canis familiaris'))

for elemento in tupla:
    print(elemento)

lista1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
lista2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
lista3 = lista1 + lista2
print(lista3)

lista2_lista22 = lista2 * 2
print(lista2_lista22)

print(lista1[0:2])

lista1.append('Gorila gorila')
print(lista1)

lista1.remove('Felis catus')
print(lista1)

del(lista1)

for item in lista2_lista22:
    print(item)

coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11
print(coleta)

del(coleta['Aedes aegypt'])
print(coleta)

print(coleta.items())

print(coleta.keys())
print(coleta.values())

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
coleta.update(coleta2)
print(coleta)

for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, Número de espécimes: {num_especimes}')
    
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidratos', 'lipídeos', 
                'ácidos nucleicos', 'carboidratos', 'lipídeos')

print(biomoleculas)
print(set(biomoleculas))

c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2)
print(c3)

print(c1.difference(c2))
print(c2.difference(c1))

















