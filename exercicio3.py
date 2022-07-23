# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:11:04 2021

@author: odp107589
"""

#Ler 5 notas e informar a média
soma_notas = 0
media_notas = 0

for i in range(1, 6):
    soma_notas += int(input(f'Digite a {i} nota: '))
media_notas = soma_notas / 5
print('A média é: ', media_notas)


#Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
for i in range(1, 11):
    print(f'3 x {i} = ', 3 * i)

numero = 1
while numero < 11:
    print(f'3 x {numero} = ', 3 * numero)
    numero += 1