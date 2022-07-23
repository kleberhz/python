# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:58:26 2021

@author: odp107589
"""

def mensagem():
    print('Texto da função')

mensagem()

def mensagem(texto):
    print(texto)

mensagem('Texto 1')

def soma(a, b):
    print(a + b)

soma(2, 3)

def soma2(a, b):
    return a + b

soma(3, 2)



def calcula_energia_potencial_gravitacional (m, h, g = 10):
    '''Descrição da função'''
    e = g * m * h
    return e

print(calcula_energia_potencial_gravitacional(30, 12))
print(calcula_energia_potencial_gravitacional(30, 12, 9.8))

help(calcula_energia_potencial_gravitacional)