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
    pero.right(90)
    nuholnik(3,a,f2)
    pero.up()
    pero.right(90)
    pero.forward(a)
    pero.left(90)


def n_farba():
    farba = "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    return farba

def ulica(rady, stlpce, a):
    pero.setpos(-350, 250)
    pero.setheading(0)
    y = 250
    for i in range(stlpce):
        for i in range(rady):
            domcek(n_farba(),n_farba(),a)
            pero.up()
            pero.forward(a*2)
        y -= 2*a
        pero.setpos(-350,y)



def nahodne_mesto(pocet):
    for i in range(pocet):
        pero.setpos(random.randint(-400,400), random.randint(-300,300))
        pero.setheading(random.randint(-10,10))
        domcek(n_farba(), n_farba(), random.randint(5,70))



tabula = turtle.Screen()
pero = turtle.Turtle()
pero.up()
pero.speed(0)
nahodne_mesto(30)
# ulica(7,3,30)
pero.hideturtle()
tabula.mainloop()
