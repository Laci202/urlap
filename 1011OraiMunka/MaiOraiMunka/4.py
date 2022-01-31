import math
print(
    """
    4.	Kérj be ellenőrzötten egy negatív számot, majd 
    add meg az abszolút értékét!
    """
)

szam=int(input("Kérlek adj meg egy számot!"))
while not(szam<0):
    szam = int(input("Kérlek adj meg egy számot!"))
print("|",szam,"|=",math.fabs(szam))