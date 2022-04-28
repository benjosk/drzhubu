import tkinter,random
def strom(vyska,jablka):
    a,b = random.randint(100,700), random.randint(100,400)
    x,y = random.randint(100,700), random.randint(100,400)
    canvas.create_line(x,500,x,y,width = vyska/3, fill="brown")
    canvas.create_oval(x-vyska,y-vyska,x+vyska,y+vyska,fill="green")
    for i in range(jablka):
        while (a-x)**2 + (b-y)**2 > vyska**2:
            a, b = random.randint(100, 700), random.randint(100, 400)
        else:
            canvas.create_oval(a-vyska/7,b-vyska/7,a+vyska/7,b+vyska/7, fill="red")
            a, b = random.randint(100, 700), random.randint(100, 400)
canvas= tkinter.Canvas(width=800,height=500)
canvas.pack()
for i in range(3):
    strom(random.randint(20,100),random.randint(1,5))
canvas.mainloop()
