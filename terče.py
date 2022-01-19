import turtle, random

def terce():
    for i in range(10):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        t.goto(x, y)
        c = 0
        subor.write(str(x)+" ")
        subor.write(str(y)+ " ")
        for i in range(10):
            farba = "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
            t.dot(50 - c, farba)
            subor.write(farba+ " ")
            if i == 9:
                subor.write("\n")
            c += 5


subor = open("terciky.txt", "w", encoding="UTF-8")
canvas = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
terce()
t.hideturtle()
subor.close()
canvas.mainloop()

