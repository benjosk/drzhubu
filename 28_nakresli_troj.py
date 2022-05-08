import math,turtle     # z kniznice pouzijeme metody:  # acos - Arkuskosinus vypocita uhol v radianoch  # degrees - premeni na stupne
def vypocitaj_uhol_x(x, y, z):          #vypocita uhol poroti strane x, cize uhol medzi stranami y,z
    cos_x = (y ** 2 + z ** 2 - x ** 2) / (2 * y * z)
    return math.degrees(math.acos(cos_x))
t = turtle.Turtle()
t.up()
t.setpos(-200,-100)
canvas = turtle.Screen()
while True:
    try:
        a = float(input("strana a: "))*10
        b = float(input("strana b: "))*10
        c = float(input("strana c: "))*10
        if a+b<c or a+c<b or c+b<a:
            raise ValueError
        break
    except ValueError:
        print("zlá hodnota")
t.down()
t.forward(c)
t.left(180)
t.right(vypocitaj_uhol_x(b,a,c))
t.forward(a)
t.left(180)
t.right(vypocitaj_uhol_x(c,a,b))
t.forward(b)
t.setheading(270)
t.up()
t.forward(20)
t.write(f"a = {a/10}, b = {b/10}, c = {c/10}")
t.forward(20)
t.write(f"alfa = {round(vypocitaj_uhol_x(a,b,c),1)}°, beta = {round((vypocitaj_uhol_x(b,a,c)),1)}°, gama = {round((vypocitaj_uhol_x(c,a,b)),1)}°")
t.hideturtle()
canvas.mainloop()
