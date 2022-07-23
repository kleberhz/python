# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:49:18 2021

@author: odp107589
"""

# print(3 = 4)

# print('Meu nome é: ', nome)

# print(3 / 0)

# print(2.3 / 'cachorro')

# c = [1, 2, 3, 4, 5]
# print(c[5])

while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except:
        print('Valor inválido')
    else:
        print(n)
        break

while True:
    try:
        p = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado é: {p}')
        break