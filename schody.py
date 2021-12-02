import turtle

canvas = turtle.Screen()
pen = turtle.Turtle()

vyska = int(canvas.textinput("Schody", "Zadaj výšku schodu"))
schody = int(canvas.textinput("Schody", "Zadaj počet schodov"))


sirka = 63-vyska*2
pen.speed(10)
pen.up()
pen.setpos(-250,-200)
pen.left(90)
pen.down()
pen.fillcolor("grey")
pen.begin_fill()
for i in range(schody):
    pen.forward(vyska)
    pen.left(-90)
    pen.forward(sirka)
    pen.left(90)

pen.right(180)
pen.forward(schody*vyska)
pen.right(90)
pen.forward(sirka*schody)
pen.end_fill()
pen.up()
pen.left(90)
pen.forward(30)
pen.right(90)

text =""
if 7 < vyska <13:
    text += "Rampové schodisko"
elif 12< vyska <15:
    text += "Mierne schodisko"
elif 14< vyska <18:
    text += "Normálne schodisko"
elif 17< vyska <20:
    text += "Strmé schodisko"
elif vyska >19:
    text += "Rebríkové schodisko"
pen.write(f"{text}, výška = {schody*vyska}, šírka = {sirka*schody}")
pen.hideturtle()

canvas.mainloop()
