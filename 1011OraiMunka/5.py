import math
print(
    """
    5.	Kérj be ellenőrzötten egy 3-mal osztható, 
    kétjegyű számot, majd add meg a négyzetét!
    """
)

szam=int(input("Kérem adjon meg egy számot!"))
harommalOszthato = szam % 3 == 0
ketjegyu= ((szam > 9) and (szam <= 99)) or ((szam >= -99) and (szam < -9))
feltetel = harommalOszthato and ketjegyu

while not(feltetel):
    szam = int(input("Kérem adjon meg egy számot!"))
    harommalOszthato = szam % 3 == 0
    ketjegyu = ((szam > 9) and (szam <= 99)) or ((szam >= -99) and (szam < -9))
    feltetel = harommalOszthato and ketjegyu
print("A szám: ",szam,"négyzet értéke: ", math.pow(szam,2))