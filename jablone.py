import turtle
import random

canvas = turtle.Screen()
pen = turtle.Turtle()

def strom(vyska, jablcko):
    pen.color("brown")
    pen.left(90)
    pen.down()
    pen.width(vyska/5)
    pen.forward((vyska+10))
    pen.up()
    pen.forward(vyska)
    pen.color("green")
    pen.dot(vyska*2)
    pen.up()
    for i in range(jablcko):
        pen.setheading(random.randint(0,360))
        cislo = random.randint(0,vyska-10)
        pen.forward(cislo)
        pen.dot(10,"red")
        pen.right(180)
        pen.forward(cislo)
    pen.setheading(0)

def sad(x,y):
    a = -200
    b = 100
    for o in range(y):
        for i in range(x):
            a +=100
            strom((random.randint(10,50)),(random.randint(1,10)))
            pen.setpos(a,b)
            if a > 300+100:
                turtle.screensize(canvwidth=600+100*x)
        a = -200
        b -= 200
        pen.setpos(a,b)
        if b < -300:
            turtle.screensize(canvheight=600+200*y)

turtle.screensize(canvwidth=600, canvheight=600)
pen.up()
pen.speed(0)
pen.setpos(-200,100)

sad(7,4)

canvas.mainloop()
