# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:59:09 2021

@author: odp107589
"""

for numero in range(1, 5):
    print(numero)

for numero2 in range(5, 0, -1):
    print(numero2)
    
soma = 0
for numero in range(1, 6):
    soma = soma + numero
    #print(soma)
print(soma)

palavra = 'sorvete'
for letra in palavra:
    #print(letra)
    if letra == 'v':
        print('achou a letra V')
        
for i in range(0, 5):
    print(i)        
    print('-----')
    for j in range(0, 3):
        print(j)
    print (i)


numero = 1
while numero < 6:
    print(numero)
    numero += 1
print('acabou')

numero2 = 5
while numero2 > 0:
    print(numero2)
    numero2 -= 1
    
soma = 0
numero = 1
while numero < 6:
    soma += numero
    numero +=1
print(soma)

numero = -1
while numero < 1 or numero > 10:
    numero = int(input('Digite um número de 1 a 10: '))













