text = input()
def prevedeni(text):
    while "(" in text:
        pozice_prvni_zavorky = text.rfind("(")
        pozice_druhe_zavorky = text.find(")", pozice_prvni_zavorky)
        vysledek_zavorky = str(finalni(trideni(prevedeni(text[pozice_prvni_zavorky + 1:pozice_druhe_zavorky]))))
        text = text[:pozice_prvni_zavorky] + vysledek_zavorky + text[pozice_druhe_zavorky + 1:]
    vysledek = []
    cislo = ""
    for char in text:
        if char.isnumeric():
            cislo += char
        else:
            if cislo:
                vysledek.append(cislo)
                cislo = ""
            vysledek.append(char)
    if cislo:
        vysledek.append(cislo)
    return vysledek

def trideni(vysledek):
    prednost = "*/"
    i = 1
    while i < len(vysledek) - 1:
        prvek = vysledek[i]
        a = float(vysledek[i+1])
        b = float(vysledek[i-1])
        if prvek in prednost:
            if prvek == "*":
                vysledek[i-1:i+2] = [str(a*b)]
            else:
                 vysledek[i-1:i+2] = [str(a/b)]
            i = 1
        else:
            i +=2
        
    return vysledek        

def finalni(vysledek):
    result = float(vysledek[0])
    znamenka = "+-"
    i = 1
    while i < len(vysledek):
        prvek = vysledek[i]
        if prvek in znamenka:
            if prvek == "+":
                result += float(vysledek[i+1])
            else:
                result -= float(vysledek[i+1])
        i += 2
    return result

try:
    print(finalni(trideni(prevedeni(text))))
except ValueError:
    print("Zadej validni input")

            