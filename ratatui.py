import random

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
    return heslo


m = int(input("pocet malych:"))
v = int(input("pocet velkych:"))
c = int(input("pocet cisel:"))
z = int(input("pocet znakov:"))


print(generuj_heslo(m,v,c,z))
