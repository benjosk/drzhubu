import turtle, random

def hodiny(f1,f2):
    t.down()
    t.color(f2)
    t.fillcolor(f1)
    t.width(10)
    t.begin_fill()
    t.setheading(60)
    t.forward(200)
    t.setheading(180)
    t.forward(100)
    t.setheading(-60)
    t.forward(200)
    t.setheading(180)
    t.forward(100)
    t.end_fill()
    t.up()
    t.setheading(0)
    t.forward(100)

def vsetky_hodiny():
    farby = ["red", "green", "blue", "orange", "yellow"]
    f1 = random.choice(farby)
    f2 = random.choice(farby)
    if f2 == f1:
        f2 = random.choice(farby)
    else:
        for i in range(5):
            hodiny(f1, f2)
            f1,f2 = f2,f1

t = turtle.Turtle()
scr = turtle.Screen()
t.up()
t.setpos(-250, -70)
vsetky_hodiny()
scr.mainloop()
