"""2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!"""
def szamozas(szam):
    if szam > 0:
        print("Ez a szám pozitív.")
    elif szam == 0:
        print("Ez a szám nulla.")
    else:
        print("Ez a szám negatív.")


folytat = True
while folytat == True:
    szam = int(input("Adj meg egy számot: "))
    szamozas(szam)
    if szam == "":
        folytat = False