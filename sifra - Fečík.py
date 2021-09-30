subor = open("diktat.txt", "r", encoding="UTF-8")
diktat = subor.read().lower()
subor2 = open("novysubor.txt", "w", encoding="UTF-8")

def zamena(posun, text):
    for pismeno in text:
        poradie = ord(pismeno)
        if poradie == 32:
            poradie = poradie
        elif poradie == 46:
            poradie = poradie
        elif poradie == 10:
            poradie = poradie
        else:
            poradie += posun
            if poradie > 122:
                zvys = 122% poradie
                poradie = 97 + zvys
        nove = chr(poradie)
        subor2.write(nove)


n = int(input("posun písmen abecedy o : "))

zamena(n,diktat)

subor2.close()
subor.close()
