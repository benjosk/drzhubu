import random


def pocitaj():
    text = diktat.lower()
    samohlasky = "aeiouáôéíóúäyý"
    cp = 0
    for pismeno in samohlasky:
        for znak in text:
            if pismeno == znak:
                cp += 1
    print(f"počet vštkých samohlások je: {cp}")

def riadky():
    r = subor.readline()
    for i in range(0, len(r), 2):
        print(r)


def generuj_heslo (pm,pv,pc,pz):
    male = "abcdefghijklmnopqrstuvwxyz"
    velke = male.upper()
    cislo = "0123456789"
    heslo = ""
    for i in range(pm):
        heslo += random.choice(male)
    for i in range(pv):
        heslo += random.choice(velke)
    for i in range(pc):
        heslo += random.choice(cislo)
    for i in range(pz):
        heslo += random.choice("+-*/?.:@&#")

    real_heslo= ""
    while len(heslo) > 0:
        i = random.randrange(len(heslo))
        real_heslo += heslo[i]
        heslo = heslo[:i] + heslo[i+1:]

    return real_heslo

def heslicko(r):
    for i in range (r):
        s2.write(generuj_heslo(3,2,2,1) + "\n")

subor = open("diktat.txt", "r", encoding="UTF-8")
diktat = subor.read()

s2 = open("novysubor.txt", "a", encoding="UTF-8")

heslicko(4)

# pocitaj()
# riadky()

subor.close()
s2.close()



