# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:57:56 2021

@author: odp107589
"""

lista = []

try:
    lista.append(float(input('Digite o primeiro número: ')))
    lista.append(float(input('Digite o segundo número: ')))
    divisao = lista[0] / lista[1]
    print(divisao)
except ValueError:
    print('Números informados inválidos')
except ZeroDivisionError:
    print('Números informados igual a zero')
except IndexError:
    print('Tentativa de divisão por posições inexistentes na lista')
except KeyboardInterrupt:
    print('Programa foi interrompido pelo usuário')
else:
    print(f'A divisão dos números é: {divisao}')