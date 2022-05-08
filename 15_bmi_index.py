import tkinter

canvas = tkinter.Canvas(height=300, width=600)
canvas.pack()

vyska = float(input("zadaj vysku v cm: "))
vaha = float(input("zadaj vahu v kg: "))
bmi = vaha/(vyska/100)**2
text = ""
farba = ""
if bmi <= 17.5:
    text+= "podvýživa"
    farba+="yellow"
if 17.5< bmi <= 25:
    text+= "ideálna a zdravá váha"
    farba+="green"
if 25 < bmi <= 30:
    text+= "mierna nadváha "
    farba+="orange"
if 30 < bmi <= 40:
    text+= "obezita "
    farba+="red"
if bmi > 40:
    text+= "tažká obezita "
    farba+="red"


canvas.create_rectangle(0,100,700,200, fill="yellow",outline="yellow")
canvas.create_rectangle(175,100,700,200, fill="green",outline="green")
canvas.create_rectangle(250,100,700,200, fill="orange",outline="orange")
canvas.create_rectangle(300,100,700,200, fill="red",outline="red")
canvas.create_line(bmi*10, 90, bmi*10, 210, width=5)
canvas.create_text(300, 50, text=f"výška: {vyska}cm, váha: {vaha}kg", font= ("Ariel" ,22, "bold"))
canvas.create_text(300,250, text=text, fill=farba, font= ("Ariel" ,18, "bold"))
canvas.create_text(300,270, text=f"BMI: {round(bmi,2)}", fill=farba, font= ("Ariel" ,18, "bold"))


canvas.mainloop()
