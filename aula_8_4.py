# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:08:37 2018

@author: mathe
"""

num = 0
x=0
x1=0
contador=0
xn=0
num = float(input('entre com o numero:'))

while num > 0:
    x1 = num/2.0
    print('| numero: %.4f | aproximação: %.4f | raiz: %.4f|' %(contador,num,x1))
    while contador <= 20:
        xn = ((x1*x1)+num)/(2*x1)
        x1 = xn
        print('| numero: %.4f | aproximação: %.4f | raiz: %.4f|' %(contador,num,x1))
        contador = contador + 1
        
    contador = 0
    num = float(input('entre com o numero'))