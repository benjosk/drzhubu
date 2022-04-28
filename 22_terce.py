import turtle,random
def terc(x,y):
    n = 50
    with open("22_terce.txt", "a") as subor:
        t.setpos(x, y)
        subor.write(str(x) + " " +str(y) + " ")
        for i in range(10):
            farba = "#" + f"{random.randrange(255):02x}" + f"{random.randrange(255):02x}" + f"{random.randrange(255):02x}"
            subor.write(farba + " ")
            t.dot(n,farba)
            n -= 5
        subor.write("\n")
t = turtle.Turtle()
t.up()
t.speed(0)
canvas = turtle.Screen()
for i in range(10):
    terc(random.randint(-300,300),random.randint(-300,300))
canvas.mainloop()
