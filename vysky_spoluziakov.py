vysky = {'Igor':197, 'Mariana':160, 'Adam':171,'Peťo':181,'Milan':161,'Pišta':155,'Fero':190,
         'Bernard':178, 'Milada':165, 'Jozefína':179,}

# for kluc,hodnota in sorted(vysky.items()):
#     print(kluc,":",hodnota)

# for kluc,hodnota in sorted(vysky.items(), key=lambda x:x[1], reverse=True):
#     print(kluc,":",hodnota)

def vypis(vysky):
    v = []
    for vyska in vysky.values():
        v.append(vyska)
    primer = sum(v)/len(v)
    for kluc,hodnota in sorted(vysky.items()):
        if hodnota < primer:
            print(f"{kluc}: {hodnota}cm - podpriemer")
        elif hodnota == primer:
            print(f"{kluc}: {hodnota}cm - priemer")
        elif hodnota > primer:
            print(f"{kluc}: {hodnota}cm - nadpriemer")

def vysky_oddo(vysky,od,do):
    vysky2 = {}
    for kluc,hodnota in sorted(vysky.items()):
        if od > do:
            od,do = do,od
        if od < hodnota < do:
            vysky2[kluc] = hodnota
    return vysky2

# vypis(vysky)
vypisovanie = vysky_oddo(vysky,160,175)

for kluc,hodnota in vypisovanie.items():
    print(f"{kluc}: {hodnota}cm")
