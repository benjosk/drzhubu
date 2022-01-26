def dasa(a,b,c)
    if a+b<c or a+c<b or c+b<a :
        print("takýto trojuholník neexistuje")
    else:
        return True

def uhly(a,b,c):


def strany(a,b,c):
    text =""
    if a == b or a == c or c == b:
        text += "rovnoramenný"
    elif a == b == c :
        text += "rovnnostranný"
    else:
        text += "rôznostranný"
    return text
