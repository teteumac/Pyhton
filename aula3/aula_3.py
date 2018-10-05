#exemplos aula 3

import math
cateto_oposto = 4
cateto_adjacente = 2
tg_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tg_theta)
print(theta, 'em radianos')
theta_graus = theta*180/math.pi
print(theta_graus)

print('\n')
##############################################################################

CO=(2)**(1/2)
H=2
coseno=CO/H
theta_graus = math.degrees(math.acos(math.sqrt(2)/2))
print(theta_graus)

##############################################################################

print('\n')

def print_poema():
    print('Caminante, no hay camino,')
    print('se hace camino al andar.')

def verso_poema():
    print('Caminante, son tus huellas')
    print('el camino y nada más;')

    print_poema()

    print('Al andar se hace el camino,')
    print('y al volver la vista atrás,')
    print('se ve la senda que nunca')
    print('se ha de volver a pisar.')
    print('Caminante no hay camino')
    print('sino estelas en la mar.')

verso_poema()

print('\n')

print('----------------------------------------------------X-------------------------------------------------------------')
