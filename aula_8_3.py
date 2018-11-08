# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:31:57 2018

@author: mathe
"""

def par_impar(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 1:  # If the number is odd
            print(lista[i], 'ímpar')
        elif lista[i] % 2 == 0:
            print(lista[i], 'par')
        
lista = [3,5,7,44,77,88,9,32,16548482,32021548,2]

par_impar(lista)
print("\nDONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")