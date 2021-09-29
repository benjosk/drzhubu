subor = open("diktat.txt", "r", encoding="UTF-8")
diktat = subor.read()
znaky = "yýiíYIÍÝ"

def zmen (text, znak):
    for znak in znaky:
        for i in range(len(text)):
            if znak == text[i]:
                text = text[:i] + "_" + text[i+1:]
    return text

# print(len(diktat))
# for riadok in subor:
#     print(riadok)

subor.close()

s2 = open("novysubor.txt", "w", encoding="UTF-8")
s2.write(zmen(diktat,znaky))
s2.close()

print(zmen(diktat,znaky))
