import tkinter

canvas = tkinter.Canvas(height = 300, width = 500, bg= "pink")
canvas.pack()

def bmi(vyska,hmotnost):
    vyska = vyska / 100
    cislo = round(hmotnost /vyska**2, 2)
    return cislo

def grafik(cislo):
    print(cislo)
    x = cislo * 10
    canvas.create_line(0,150,175,150, width=50, fill="yellow")
    canvas.create_line(175,150,250,150, width=50, fill="green")
    canvas.create_line(250,150,300,150, width=50,fill="orange")
    canvas.create_line(300,150,500,150, width=50, fill="red")
    if 0 < cislo < 17.49:
        farba = "yellow"
        text = "podvíživa" + "\n" + "BMI = " + str(cislo)
    if 17.5 < cislo < 24.99:
        farba = "green"
        text = "ideálna a zdravá váha" + "\n" + "BMI = " + str(cislo)
    if 25 < cislo < 29.99:
        farba = "orange"
        text = "mierna nadváha" + "\n" + "BMI = " + str(cislo)
    elif 30 < cislo:
        farba = "red"
        text = "ťažká obezita" + "\n" + "BMI = " + str(cislo)
    canvas.create_line(x,120,x,180, width = 3)
    canvas.create_text(250,250, text = text, fill=farba, font="Ariel, 15")
    canvas.create_text(250,80, text = f"výška: {vyska} cm,  hmotnosť: {hmotnost} kg", font="Ariel, 15")

vyska = float(input("zadaj výšku v cm:"))
hmotnost = float(input("zadaj váhu v kg:"))

grafik(bmi(vyska,hmotnost))

canvas.mainloop()
