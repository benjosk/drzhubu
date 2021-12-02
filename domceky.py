import turtle
import random

def nuholnik(n, a, farba):
    pero.down()
    uhol = (n-2)*180
    uhol = 180-(uhol / n)
    pero.fillcolor(farba)
    pero.begin_fill()
    for i in range(n):
        pero.forward(a)
        pero.left(uhol)
    pero.end_fill()
    pero.up()

def domcek(f1, f2, a):
    nuholnik(4,a,f1)
    pero.left(90)
    pero.forward(a)
    nuholnik(3,a,f2)

# def n_farba():
#
# def ulica(rady, stlpce, a):
#
# def nahodne_mesto(pocet):

tabula = turtle.Screen()
pero = turtle.Turtle()
#ulica(7, 3, 30)
#nahodne_mesto(30)
domcek("red","green",50)
pero.hideturtle()
tabula.mainloop()
