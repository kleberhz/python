# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:41:26 2021

@author: odp107589
"""

# Crie um arquivo .py com duas funções
# - Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o 
#                              usuário digitou)
# - Função para ler um número float (recebe como parâmetro uma mensagem e retorna o 
#                                    que o usuário digitou)

# Importar o arquivo criado no Google Colab e testar as funções

import exercicio6_funcoes as leitura

texto = leitura.ler_texto('Digite o seu nome: ')
print(texto)

carro = leitura.ler_texto('Digite o nome do seu carro: ')
print(carro)

numero = leitura.ler_numero('Digite sua idade: ')
print(numero)