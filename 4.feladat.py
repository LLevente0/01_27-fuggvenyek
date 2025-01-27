"""4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót
, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a
képernyőre kiírja, melyik a legrövidebb szó!"""

szavak = []
hanyszor = 5

def szo_hozzaadas():
    bekert_szo = input("Adj meg egy szót: ")
    szavak.append(bekert_szo)

    print(szavak)

folytat = True
while len(szavak) < hanyszor:
    szo_hozzaadas()
    folytat == True
    if len(szavak) == hanyszor:
        folytat == False

szavak.sort()
print(f"\nA legrövidebb szó: {szavak[0]}")