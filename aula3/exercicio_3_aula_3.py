print('exercicío 3: Crie uma funcão para calcular o ângulo zenital do sol (da semana passada) \n'
      'tomando como argumento as medidas da altura e o comprimento da sombra.\n')

import math
cateto_oposto = 0.5
cateto_adjacente = 5
tg_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tg_theta)
print(theta, 'em radianos')
theta2=math.degrees(theta)
print(theta2, 'graus')
