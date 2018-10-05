print('exercicío 2: Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial\n'
      'e final e o tempo transcorrido para um objeto em MRU. Também crie uma funcão que calcule e imprima a velocidade de um\n'
      'objeto a partir da aceleração constante e o tempo (MRUA) (p.ex. queda libre).\n')

def velocidade_media(x0, x, t):
    Vm=(x-x0)/t
    print('Vm =', Vm, 'anos luz/séculos')

velocidade_media(2,10,5)

def velocidade_media_2(v0, a, t2):
    Vf=v0+a*t2
    print('Vm =', Vf, 'anos luz/séculos')

velocidade_media_2(0,2,3)
