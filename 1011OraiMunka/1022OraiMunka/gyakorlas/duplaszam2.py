print(
    """
    2.	Duplaszam2:A program írja ki az első N darab 
    természetes szám összegét! Bemenetként ne fogadjon el 
    negatív számot! A megoldás tartalmazzon egy olyan 
    függvényt, amely paraméterként átveszi a beolvasott 
    számot, és saját maga számítja és írja ki annak 
    kétszeresét!
    """
)

def ketszeres(szam):
    ketszerese=szam*2
    return ketszerese

n=int(input("Kérem adjon meg egy természetes számot!"))
while not(n>=0):
    n = int(input("Kérem adjon meg egy természetes számot!"))
osszeg=0
for i in range(0,n):
    osszeg+=i
print("Az első n természetes szám összege:",osszeg)



