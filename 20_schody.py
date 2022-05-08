import turtle

def schod(sirka,vyska):
    t.left(90)
    t.forward(vyska)
    t.right(90)
    t.forward(sirka)

t = turtle.Turtle()
canvas = turtle.Screen()
typ=""
while True:
    try:
        pocet = int(input("počet schodov: "))
        vyska = int(input("výška chodu: "))
        if 8 <= vyska < 13:
            typ+= "Rampové"
        elif 13 <= vyska <15:
            typ += "Mierne"
        elif 16<= vyska < 18:
            typ += "Normálne"
        elif 18 <= vyska <20:
            typ += "Strmé"
        elif 20 <= vyska <= 25:
            typ+= "Rebríkové"
        else:
            raise ValueError
        break
    except ValueError:
        print("zlá hodnota")


sirka = 63 - 2*vyska
t.up()
t.setpos(-250,-200)
t.down()
for i in range(pocet):
    schod(sirka,vyska)
t.right(90)
t.forward(vyska*pocet)
t.right(90)
t.forward(sirka*pocet)
t.up()
t.setpos(-250,-220)
t.write(f"{typ}: výška: {vyska*pocet}cm, šírka: {sirka*pocet}cm")
t.hideturtle()


canvas.mainloop()
