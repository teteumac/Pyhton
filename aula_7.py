# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:48:52 2018

@author: mathe
"""

import turtle
import math
def draw_bar(t, mini, maxi, binn, dados):
    """ Get turtle t to draw one bar, of height. """
    height= []
    if mini >= maxi:
        print('Deu erro pq não tem como o valor mínimo ser maior que máximo né? Se não seria maximo e não mínimo')
    if type(dados)!= tuple:
        print('Os dados precisam ser uma lista para fazer um histograma')
        
    bin_size = (maxi - mini)/binn
    n = len(dados)
    altura = 0 
    for i in range(0,int(binn)):
        for dado in dados:
            if(dado<mini or dado>maxi):
                print('ERRO')
            if dado >= mini + bin_size*i and dado < mini + bin_size*(i+1):
                altura +=1
        height.append(altura)
        altura = 0
        
    j = len(height)
    print('len(height)=',j)
    print(height)
    for n in range(0,j):
        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height[n])
        t.write("  "+ str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height[n])
        t.left(90)
        t.end_fill()             # Added this line
        t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

dados = (1,2,3,4,15,30,14,7,7,8,3,26,24,38,98,89,27,782)


draw_bar(tess,0,100,899,dados)

wn.mainloop()