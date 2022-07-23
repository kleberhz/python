# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:14:19 2021

@author: odp107589
"""

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0
        
    def calcular(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media
    
    def mostraDados(self):
        print('Nome: ', self.nome)
        print('Nota 1: ', self.nota1)
        print('Nota 2: ', self.nota2)
        print('Média: ', self.media)
    
    def resultado(self):
        if self.media >= 6.0:
            return 'Aprovado'
        else:
            return 'Reprovado'
        
aluno1 = Aluno('Teste Aluno 1', 5, 7)
aluno1.calcular()
aluno1.mostraDados()
print(aluno1.resultado())

print('---------------------')

aluno2 = Aluno('Teste Aluno 2', 4, 3)
aluno2.calcular()
aluno2.mostraDados()
print(aluno2.resultado())