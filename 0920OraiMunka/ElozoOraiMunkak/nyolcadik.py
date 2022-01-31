print(
    """
Írj egy Python programot az előző feladat
általános megoldására. Kérd be a felhasználótól
az aktuális időt (csak az órákat) és azt, hogy
hány órával később szólaljon meg az ébresztőóra,
majd jelenítsd meg a képernyőn, hogy hány órakor
fog megszólalni az ébresztőóra.
    """
)
from math import *
most=int(input("Kérem adja meg a jelenlegi időt (órában)!"))
kesobb=int(input("Kérem adja meg, hogy hány órát alszik!"))
osszeg=most+kesobb
felkelesNap=floor(osszeg/24)
#felkelesNap2=int(51/14)
felkelesOra=osszeg%24
print("A megadott adatok alapján: "+str(felkelesNap)+" nap "+str(felkelesOra)+" órakkor fog felébredni.")