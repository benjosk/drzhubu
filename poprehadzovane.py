import random
text = "Prezidentka SR Zuzana Čaputová, premiér Eduard Heger a predseda parlamentu Boris Kollár včera diskutovali v Prezidentskom paláci o aktuálnej medzinárodnej situácii v súvislosti s krízou na Ukrajine a o dosahoch na Slovensko."
t = text.split()
zoz =[]
def split(word):
    return [char for char in word]
for slovo in t:
    pismena = split(slovo)
    pismena = pismena[1:-1]
    pis=""
    for i in range(len(pismena)):
        p = random.choice(pismena)
        pismena.remove(p)
        pis += p
    rez = slovo[0] + pis + slovo[-1]
    print(rez)
