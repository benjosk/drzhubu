import tkinter

with open ("preklopenie.txt") as f:
    rozmery = f.readline().split()
    lines = f.read().replace(' ', '')
    subor = lines.splitlines()

canvas = tkinter.Canvas(width=rozmery[0], height=rozmery[1])
canvas.pack()

def kresli(strana):
    x,y = 0,0
    for j in range(len(subor)):
        for znak in subor[j]:
            if znak == "1":
                canvas.create_rectangle(x, y, x + strana, y, fill="black")
            if znak == 0:
                canvas.create_rectangle(x, y, x + strana, y, fill="white")
            x += strana
        x = 0
        y+= strana

def prekl():
    global subor
    subor = []
    for line in lines.splitlines():
        subor.append(line[::-1])
    canvas.delete("all")
    kresli(1)

print(f"Obrázok obsahuje {len(lines)} pixelov, z toho {lines.count('1')} je čiernych")
button1 = tkinter.Button(text='preklop', command=prekl)
button1.pack()
kresli(1)
canvas.mainloop()
