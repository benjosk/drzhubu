import tkinter
subor = open("mozaika.txt", "r", encoding="UTF-8")
text = subor.readlines()

canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()

def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = int(text[0])
    i = 1
    while y < vyska_platna + a:
        while x < sirka_platna +a:
            farba = text[i].strip()
            canvas.create_rectangle(x,y,x+a,y+a, fill=farba, outline=farba)
            i += 1
            x += a
        x = 0
        y += a

mozaika(600,400)
subor.close()
canvas.mainloop()
