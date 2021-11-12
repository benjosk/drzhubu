import tkinter
import math

def rovnica(a,b,c):
    try:
        d = b*b - (4*a*c)
        print("diskriminant =",d)
        odm = math.sqrt(d)
        x1 = -b + odm / 2*a
        x2 = -b - odm / 2*a
        if x1 == x2:
            print(f"rovnica má jedno riešenie: x = {round(x1,2)}")
        else:
            print(f"rovnica má dve riešenia: x1 = {round(x1,2)}, x2 = {round(x2,2)}")
    except ValueError:
        print("nedá sa vypočítať (záporný diskriminant)")
    canvas.create_line(0,200,400,200)
    canvas.create_line(200,20,200,400)

canvas = tkinter.Canvas(height = 400, width = 400, bg= "pink")
canvas.pack()

# a, b, c = float(input("a =")),float(input("b =")),float(input("c ="))
a,b,c = 1,-3,2

rovnica(a,b,c)

canvas.mainloop()
