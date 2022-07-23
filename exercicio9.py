# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:06:23 2021

@author: odp107589
"""

texto = "Minha casa fica na rua Reinaldo Ceschini, 572. O CEP é 06246-150 e meu site é https://www.teste.com.br"

import re

print(re.findall('\d', texto))

print(re.findall('\d{5}-\d{3}', texto))

print(re.findall('https?://[A-Za-z0-9./]+', texto))