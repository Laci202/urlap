print(
    """
    Jelenleg pontosan 14 óra van. Beállítunk
    egy ébresztőórát úgy, hogy 51 órával később
    csörögjön. Hány órakor fog az ébresztőóra
    megszólalni? (Segítség: Ha túlzottan vonz
    a lehetőség, hogy az ujjaidon számold ki,
    akkor 51 helyett dolgozz 5100-zal.)
    """
)
from math import *
most=14
kesobb=51
osszeg=most+kesobb
felkelesNap=floor(osszeg/24)
#felkelesNap2=int(51/14)
felkelesOra=osszeg%24
print("A megadott adatok alapján: "+str(felkelesNap)+" nap "+str(felkelesOra)+" órakkor fog felébredni.")