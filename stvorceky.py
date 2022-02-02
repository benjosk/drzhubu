import tkinter

def kresli(x,y,farba,strana):
    canvas.create_rectangle(x,y,x+strana,y+strana, fill= farba)

canvas = tkinter.Canvas(height = 300, width = 300)
canvas.pack()

with open("stvorceky.csv", "r") as file:
    hlavicka = file.readline()
    for riadok in file:
        x,y,f,v = riadok.split(";")
        x,y,f,v = int(x), int(y), str(f), int(v)
        kresli(x,y,f,v)

canvas.mainloop()
