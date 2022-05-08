import turtle,random
def domcek(a):
    t.down()
    t.fillcolor(farba())
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.fillcolor(farba())
    t.begin_fill()
    t.left(60)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(120)
    t.end_fill()
    t.up()
    t.forward(a)
    t.left(180)
def farba():
    f = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"
    return f
def mesto():
    for i in range(20):
        t.setpos(random.randint(-350,350),random.randint(-350,350) )
        uhol = random.randint(-30,30)
        t.setheading(uhol)
        domcek(random.randint(20,100))
t = turtle.Turtle()
t.speed(0)
t.up()
canvas = turtle.Screen()
mesto()
canvas.mainloop()
