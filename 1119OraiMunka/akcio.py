import random
print(
"""
1.	Nyerogep1: Kérj be a felhasználótól egy összeget,
 és véletlenül sorsolj ki egy akció értéket 1% és 
 50% között. Majd írd ki a felhasználónak 2 
 tizedesjegyre kerekítve a megtakarított összeget, 
 és a fizetendőt egész értékként!
"""
)
# Ft gondoljuk az öszeget
osszeg=int(input("Kérem adjon meg egy összeget(Ft-ba)."))
akcio=random.randint(1,50)
akcioFtBan=osszeg*akcio/100
vegsoOsszeg=osszeg*(1-(akcio/100))
#print("Az akció mértéke: '{1}', százalékban: '{0}'".format(akcio,akcioFtBan))
print("Az akció mértéke: {}, százalékban: {:.0%}".format(akcioFtBan,akcio/100))


