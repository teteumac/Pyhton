import math

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