import tkinter
canvas = tkinter.Canvas(width=200, height=400, bg="black")
canvas.pack()

def pridaj():
    global c
    if c <= 270:
        canvas.create_rectangle(80,0,190,400, fill="black")
        canvas.create_rectangle(80,0,190,c+10, fill="red")
        c = c+10
    else:
        print("spomal ne")

def spomal():
    global c
    if c >= 10:
        canvas.create_rectangle(80,0,190,500, fill="black")
        canvas.create_rectangle(80,0,190,c-10, fill="red")
        c = c-10
    else:
        print("práve stojíš v strede cesty")

c = 100
x,y = 20, 10
cislo = 0
for i in range(20):
    canvas.create_text(x,y, tex=cislo, fill="white")
    canvas.create_line(x-20,y+7, x+50,y+7, fill="white")
    cislo += 10
    y += 20

canvas.create_rectangle(80, 0, 190, c, fill="red")

button1 = tkinter.Button(text='rýchlejšie', command=pridaj)
button1.pack()
button2 = tkinter.Button(text='pomalšie', command=spomal)
button2.pack()

canvas.mainloop()
