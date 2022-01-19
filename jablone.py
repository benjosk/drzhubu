import turtle
import random

canvas = turtle.Screen()
pen = turtle.Turtle()

sirka = int(canvas.numinput("Stromy", "Zadaj počet stromov v rade"))
vyska = int(canvas.numinput("Stromy", "Zadaj počet stromov v stĺpci"))

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
    a = -300
    b = 100
    for o in range(y):
        for i in range(x):
            a +=100
            strom((random.randint(15,50)),(random.randint(1,6)))
            pen.setpos(a,b)
            if a > 300+100:
                turtle.screensize(canvwidth=600+100*x)
        a = -300
        b -= 200
        pen.setpos(a,b)
        if b < -300:
            turtle.screensize(canvheight=600+200*y)


turtle.screensize(canvwidth=600, canvheight=600)
pen.up()
pen.speed(0)
pen.setpos(-300,100)
if sirka < 1:
    print("zadaj číslo väčšie ako 0")
elif vyska < 1:
    print("zadaj číslo väčšie ako 0")
else:
    sad(sirka,vyska)

pen.hideturtle()
canvas.mainloop()
