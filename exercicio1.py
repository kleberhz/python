# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:15:17 2021

@author: odp107589
"""

# 1 Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: 
#     adição, subtração, multiplicação e divisão

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print('A soma dos números é: ', numero1 + numero2)
print('A subtração dos números é: ', numero1 - numero2)
print('A multiplicação dos números é: ', numero1 * numero2)
print('A divisão dos números é: ', numero1 / numero2)

# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, 
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário 
# deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, 
# será possível obter a distância percorrida com a fórmula 
# DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a 
# quantidade de litros de combustível utilizada na viagem, com a fórmula: 
# LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da 
# velocidade média, tempo gasto na viagem, a distância percorrida e a 
# quantidade de litros utilizada na viagem

autonomia = 12

tempo = float(input('Digite o tempo gasto na viagem: '))
velocidade_media = float(input('Digite a velocidade média da viagem: '))

distancia = tempo * velocidade_media

litros_usados = distancia / autonomia

print('A velocidade média foi: ', velocidade_media)
print('O tempo gasto foi: ', tempo)
print('A distancia percorrida foi: ', distancia)
print('A quantidade de litros gasto foi: ', round(litros_usados, 1))