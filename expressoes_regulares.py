# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:53:46 2021

@author: odp107589
"""

import re

frase = 'Olá, meu número de telefone é (11)96352-2240'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase))

frase = 'A placa de carro que eu anotei durante o acidente foi GBK-3746'
print(re.search('[A-Za-z]{3}-\d{4}', frase))

email = 'Entre em contato, meu e-mail é kleberhz@hotmail.com'
print(re.search('\w+@\w+\.com', email))

frase = 'A placa de carro que eu anotei durante a batida foi GBK-3746'
print(re.match('[A-Za-z]{3}-\d{4}', frase))

frase2 = 'GBK-3746 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase2))

frase3 = 'Meu número de telefone atual é (11)96352-2240. O número (11)91234-5678 é antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Teste 1
email = teste1@teste.com
Nome: Teste 2
email = teste2@teste.com
Nome = Teste 3
email = teste3@teste.com.br'''
print(re.findall('\w+@\w+\.\w+', emails))