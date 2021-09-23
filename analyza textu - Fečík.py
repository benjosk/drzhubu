abeceda = 'aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž'
text = 'Aj v tomto školskom roku naše gymnázium ponúka možnosť vzdelávať sa vo voľnočasovom programe s názvom Akadémia veľkých diel'

for pismeno in abeceda:
    pocet = 0
    for znak in text.lower():
        if pismeno == znak:
            pocet += 1
    print(f"{pismeno}: {pocet}")
