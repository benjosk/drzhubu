import tkinter

subor = open("sen.txt", "r")
text = subor.read().split()

canvas = tkinter.Canvas(width=text[0], height=text[1], bg="white")
canvas.pack()

farby = list(text[2])
print(farby)

def mozaika():
    x,y = 1,1
    a = 10
    i = 1
    while y < int(text[1]):
        while x < int(text[0]):
            canvas.create_rectangle(x,y,x+a,y+a)
            i += 1
            x += a
        x = 1
        y += a

mozaika()
canvas.mainloop()
