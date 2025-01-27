"""2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!"""
def szamozas():
    if szam > 0:
        print("Ez a szám pozitív.")
    elif szam == 0:
        print("Ez a szám nulla.")
    else:
        print("Ez a szám negatív.")


szam = int(input("Adj meg egy számot: "))
szamozas()