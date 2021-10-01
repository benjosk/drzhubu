import random
def nazov(pocetP):
    samohlasky = "aeiouáôéíóúäyý"
    spoluhlasky = "hchkgdtnlďťňľdžčžšdzcjbmprsvz"
    nazov = ""
    sam= random.choice(samohlasky)
    nazov += sam.upper()
    nazov += random.choice(spoluhlasky)*pocetP
    nazov += sam
    return nazov

# def skupiny():


n = int(input("pocet pismen:"))

subor = open("fečík.txt", "a", encoding="UTF-8")
subor.write(nazov(n) + "\n")
nazov(n)
subor.close()

subor1 = open("fečík.txt", "r", encoding="UTF-8")
text = subor1.read()
nazvy = text.split()
print("počet skupín=", len(nazvy))
