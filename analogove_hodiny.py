import random, turtle
def kresli_hodiny():
    t.goto(0,-200)
    t.fillcolor("navy")
    t.color("navy")
    t.begin_fill()
    t.down()
    t.circle(200)
    t.end_fill()
    t.color("gold")
    t.width(5)
    t.left(90)
    t.forward(10)
    t.up()
    t.goto(-200,0)
    t.right(90)
    t.down()
    t.forward(10)
    t.up()
    t.goto(0,200)
    t.down()
    t.right(90)
    t.forward(10)
    t.up()
    t.goto(200,0)
    t.down()
    t.right(90)
    t.forward(10)
    t.up()
    t.goto(0, 160)
    val = 0
    for i in range(12):
        val += 1
        t.penup()
        t.setheading(-30 * (i + 3) + 75)
        t.forward(60)
        t.forward(20)
        t.penup()
        t.forward(10)
        t.write(str(val), align="center",font=("Arial", 12, "bold"))
    t.goto(0,0)
    x = 40
    f1, f2 = "gold", "black"
    while x > 0:
        t.dot(x)
        t.color(f1)
        x -= 5
        f1,f2 = f2,f1
    t.up()
    t.color("gold")
    t.goto(40,-150)
    t.width(6)
    t.down()
    t.circle(150)
    t.up()

def rucicky(hod,min):
    t.color("gold")
    t.goto(0,0)
    t.setheading(90)
    t.width(7)
    t.down()
    t.setheading(-(360/12*hod)+90)
    t.forward(65)
    t.up()
    t.goto(0, 0)
    t.width(4)
    t.down()
    t.setheading(-(360 / 60 *min)+90)
    t.forward(90)


def vypis_cas(h,m):
    t.color("black")
    cas = f"{h:02}:{m:02}"
    t.up()
    t.goto(0,0)
    t.setheading(90)
    t.forward(220)
    t.write(cas, align="center", font=("Arial",20))
    t.forward(-220)

canvas = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
hod, min = 18,25
kresli_hodiny()
rucicky(hod, min)
vypis_cas(hod, min)
t.hideturtle()
canvas.mainloop()
