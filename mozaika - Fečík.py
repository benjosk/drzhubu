import tkinter
import random
subor = open("mozaika.txt", "w", encoding="UTF-8")

canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()

def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = random.randrange(1,51)
    subor.write(str(a)+"\n")
    while y < vyska_platna + a:
        while x < sirka_platna +a:
            farba = f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"
            subor.write(farba+"\n")
            canvas.create_rectangle(x,y,x+a,y+a, fill=farba, outline=farba)
            x += a
        x = 0
        y += a


mozaika(600,400)
subor.close()
canvas.mainloop()
