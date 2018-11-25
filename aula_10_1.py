# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:59:34 2018

@author: mathe
"""
print('_____________________________________________\n')

print('exercício 1')

print('_____________________________________________\n')

def dobrar_elementos(uma_lista):
    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais.
    """
    
    coisas = []
    for (i,valor) in enumerate (uma_lista):
        novo_elem = 2 * valor
        coisas.append(novo_elem)

    return coisas

minha_lista =  [2,4,6]
print(minha_lista)
dobrar_elementos(minha_lista)
print(minha_lista)

help(dobrar_elementos)

print('-------------------------------------X------------------------------------------')

print('\n')

print('_____________________________________________\n')

print('exercício 2')

print('_____________________________________________\n')

cont=[1]

for i in range(1,1000):
    cont.append(cont[i-1]+1)

print(cont)    


print('-------------------------------------X------------------------------------------')

print('\n')

print('_____________________________________________\n')

print('exercício 3')

print('_____________________________________________\n')

n = input('escolha um número maior do que 101: ')
n = int(n)

while n<101:
	n = input('INSIRA UM NÚMERO MAIOR QUE 101: ')
	n = int(n)

for i in range (101,n):
	if i%21 == 0:
            print('o menor número entre 101 e', n, 'divisível por 21 é:', i)
            break
            
            
print('_____________________________________________\n')

print('exercício 4')

print('_____________________________________________\n')


linha1 = [-1,0,0,0]
linha2 = [0,1,0,0]
linha3 = [0,0,1,0]
linha4 = [0,0,0,1]

matrizEta = [coluna1,
             coluna2,
             coluna3,
             coluna4]

print(chr(951),'=') #O código chr(951) representa a letra grega Eta
for i in range (0,4):
    print(matrizEta[i])

print('\n')
print(chr(951), '3x3', '-->', matrizEta[3][3])    