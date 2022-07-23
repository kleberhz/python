# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:20:37 2021

@author: odp107589
"""

#Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números 
#inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura 
#de repetição para somar todos os valores digitados

lista = []

for _ in range (1, 6):
    valor = int(input('Digite o valor: '))
    lista.append(valor)

soma = 0

for i in range(len(lista)):
    soma += lista[i]
print(soma)

import numpy as np
print(np.array(lista).sum())


#Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, 
#fazendo a leitura dos valores por meio de uma estrutura de repetição. 
#Depois, crie uma nova estrutura de repetição para somar todas as notas e 
#retornar a média

alunos = {}
for _ in range(1, 4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota
    
soma = 0
for nota in alunos.values():
    soma += nota
print('Média: ', soma / 3)

#Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer 
#e somar todos os elementos da matriz
#matriz = np.array([[3, 4, 1],
#                   [3, 1, 5]])

import numpy as np
matriz = np.array([[3, 4, 1], [3, 1, 5]])
soma = 0
for i in range(matriz.shape[0]):
    for j in range (matriz.shape[1]):
        soma += matriz[i][j]
print('Soma: ', soma)