# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:08:36 2021

@author: odp107589
"""

import math

print(math.sqrt(9))
print(math.sin(45))
print(math.cos(45))
print(math.log(1000, 10))
print(math.log(32, 2))
print(math.log(1000))
print(math.e)
print(math.pi)

import datetime

print(dir(datetime))
print(datetime.date.today())
print(datetime.date(2020, 1, 1))
print(datetime.datetime.now())
data = datetime.date(2021, 10, 31)
print(data)
print(data.day)
print(data.month)
print(data.year)
horario = datetime.datetime(2021, 10, 31, 22, 34)
print(horario)
print(horario.hour)
print(horario.minute)
print(horario.second)

import random

print(random.random())
print(random.randint(1, 5))
print(random.randrange(0, 10, 2))
print(random.randrange(0, 10, 3))
x = ['K', 'd', 13, '34-j', 'x']
print(x)
print(random.choice(x))

import time as tm

print(tm.time())
antes = tm.time()
lista = []
for i in range(0, 10000):
    lista.append(i)

depois = tm.time()

intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

print('Finalizando.....')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')