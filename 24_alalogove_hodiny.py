import turtle
def kresli_hodiny():
    t.dot(400,"grey")
    t.dot(20,"black")
    uhol = 60
    for i in range(12):
        t.setheading(uhol)
        t.up()
        t.forward(180)
        t.down()
        t.write(i+1)
        t.forward(20)
        t.up()
        t.left(180)
        t.forward(200)
        uhol -= 30
def rucicky(hod,min):
    uhol_hod = hod*30+90-min*0.5
    t.setheading(uhol_hod)
    t.down()
    t.color("black")
    t.width(10)
    t.forward(70)
    t.setpos(0,0)
    t.setheading(-min*6+90)
    t.width(5)
    t.down()
    t.forward(100)
def vypis_cas(h,m):
    t.color("black")
    cas = f"{h:02}:{m:02}"
    t.up()
    t.goto(0,0)
    t.setheading(90)
    t.forward(220)
    t.write(cas, align="center", font=("Arial",20,"bold"))
    t.forward(-220)
canvas = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
hod, min = 18,47
kresli_hodiny()
rucicky(hod,min)
vypis_cas(hod, min)
t.hideturtle()
canvas.mainloop()
