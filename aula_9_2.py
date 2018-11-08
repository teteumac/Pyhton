# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:28:37 2018

@author: mathe
"""

#precisamos do algoritmo do primeiro exercicio para fazer o segundo
d1=5
v1=12
v1=v1/60 #dividindo a velocidade pelo tempo, a cada 1 min vai me retornar um valor de v1 para a lista

T1=d1/v1
T1=T1//1
T1=int(float(T1))+1

lista_T = []
lista_d = []

for i in range(T1):
    lista_T.append(i)
    lista_d.append(v1*i)
###############################################################################
vi=12
vi/=60
vf=15
vf/=60

d2=0.2
a= (vf**2 - vi**2)/(2*d2)

T2=(vf-vi)/a

j=0
while (j<(T2-0.1)):
    lista_d.append(5+vi*(i+0.05)+(i+0.05)+((a)*((i+0.05)**2))/2)
    print 
    lista_T.append(i+0.05+T1)
    i+=0.05

d3=7-5.2
v3=15
v3/=60

T3=d3/v3
T3=T3//1
T3_int=int(float(T3))+1

for i in range (T3_int):
    lista_T.append(i+T1+T2)
    lista_d.append(5.2+v3*i)
    
for n in range (len(lista_d)):
    print ("%.2f" % lista_d[n], "%.2f" % lista_T[n])

 



    