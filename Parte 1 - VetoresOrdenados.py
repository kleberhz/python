# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:00:26 2022

@author: odp107589
"""

import numpy as np

class VetorOrdenado:
    def __init(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = 1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores(i))
                
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
    posicao = 0
    for i in range(self.ultima_posicao + 1):
        posicao = i
        if self.valores[i] > valor:
            break
        
    x = self.ultima_posicao
    while x >= posicao:
        self.valores[x + 1] = self.valores[x]
        x -= 1