# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:05:23 2021

@author: odp107589
"""

with open('C:/Users/odp107589/.spyder-py3/manipulacao_texto_frases.py') as tex:
    for linha in tex:
        print(linha)
        
with open('C:/Users/odp107589/.spyder-py3/manipulacao_texto_frases.py') as tex:
    r = tex.readlines()
    print(r)
    
with open('C:/Users/odp107589/.spyder-py3/manipulacao_texto_frases_2.py', 'w') as texto:
    texto.write('Olá a todos')