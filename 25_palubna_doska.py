import tkinter

def rych():
    global y
    if y <= 290:
        y += 10
        canvas.create_rectangle(80, 0, 250,500, fill="black")
        canvas.create_rectangle(80, 0, 200,y, fill="red")
    else:
        print("ideš veľmi rýchlo")

def pom():
    global y
    if y >= 40:
        y -= 10
        canvas.create_rectangle(80, 0, 250,500, fill="black")
        canvas.create_rectangle(80, 0, 200,y, fill="red")
    else:
        print("pridaj trochu")

def stupnica():
    n = 0
    y = 30
    for i in range(19):
        canvas.create_text(45,y, text = n,fill="white")
        canvas.create_line(0,y+5,70,y+5, fill= "white")
        y += 20
        n += 10

canvas = tkinter.Canvas(width=300,height=500, bg="black")
canvas.pack()
y = 115
canvas.create_rectangle(80, 0, 200,y, fill="red")
t1 = tkinter.Button(text="rýchlejšie", command=rych)
t1.pack()

t2 = tkinter.Button(text="pomalšie", command=pom)
t2.pack()
stupnica()

canvas.mainloop()
