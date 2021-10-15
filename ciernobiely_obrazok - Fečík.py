import tkinter
import random

subor = open("sen.txt", "r")
text = subor.read().splitlines()
rozmery = str(text[0]).split()
sirka, vyska = int(rozmery[0]), int(rozmery[1])
text2 = text[1:]
print(text2)
znaky = []
for j in text2:
    for i in range(0, len(text)-1, 2):
        znaky.append(j[i] + j[i+1])

print(znaky)


def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = 10
    while y < vyska_platna + a:
        while x < sirka_platna +a:
            farba = f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"
            canvas.create_rectangle(x,y,x+a,y+a, fill=farba, outline=farba)
            x += a
        x = 0
        y += a

canvas = tkinter.Canvas(width=sirka, height=vyska, bg="white")
canvas.pack()
canvas.mainloop()
