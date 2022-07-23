# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:11:59 2021

@author: odp107589
"""

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('C:/Users/odp107589/.spyder-py3/exercicio_8_alunos.py', 'w') as arquivo:
   for aluno, nota in alunos.items():
       arquivo.write(f'{aluno}, {nota}\n')
    
with open('C:/Users/odp107589/.spyder-py3/exercicio_8_alunos.py') as arquivo:
    for linha in arquivo:
        print(linha)