import tkinter
import random
canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()

width = 600
a = 40
farba = print(f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}")
x,y = 0,0

for i in range(int(400/20)):
    for i in range(int(600/20)):
        canvas.create_rectangle(x,y,x+20,y+20, fill=_from_rgb((farba))
        x += 20
    x = 0
    y += 20



canvas.mainloop()
