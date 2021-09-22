# text = "lastovička"
# t1 = text[:2] + "STO" + text[5:]
# print(t1)

# for i in range(len(meno)):
#     print(meno, end=" ")
#
# for i in range(len(meno)):
#     print(meno)

# print("*" * (len(meno)+6))
# print(f"*  {meno}  *")
# print("*" * (len(meno)+6))

# meno = input("meno:")
# for i in range (len(meno)):
#     print(meno[i] * (i+1))

def sekaj(text, cislo):
    i = 0
    while i <= len(text):
        i += cislo
        text = text[:i] + "\n" + text[i:]
        i += 1
    return(text)

x = int(input("cislo:"))
hym = "Nad Tatrou sa blýska, hromy divo bijú, zastavme ich, bratia, veď sa ony stratia, Slováci ožijú."


print(sekaj(hym,x))

