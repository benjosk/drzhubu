import tkinter,random

def kruh(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r, fill="brown")

def klik(event):
    farba = random.choice(["red", "white", "yellow"])
    farba2 = random.choice(["pink", "white", "yellow"])
    x,y = event.x, event.y
    if (x-300)**2 + (y-600)**2 <= 300**2:
        canvas.create_oval(x - 10, y + 10, x + 10, y - 10, fill=farba)
        canvas.create_polygon(x,y - 5, x - 15, y + 30, x + 15, y + 30, fill=farba)
    else:
        r = random.randrange(2)
        canvas.create_oval(x - 15, y + 10, x + 15, y - 10, fill=farba2)
        if r == 0:
            canvas.create_polygon(x - 15, y, x - 20, y - 10, x - 20, y + 10, fill=farba2)
        else:
            canvas.create_polygon(x + 15, y, x + 20, y - 10, x + 20, y + 10, fill=farba2)

canvas = tkinter.Canvas(height=500, width=600, bg="blue")
canvas.pack()

kruh(300,600,300)

canvas.bind("<Button-1>",klik)


canvas.mainloop()
