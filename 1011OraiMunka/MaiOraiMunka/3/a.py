import random
print(
"""
3.	A program  kérjen be a konzolról egy valós számot! 
Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög 
mértéke (pl. 60 fok), egyébként a program adjon 
hibaüzenetet! Ha lehet, a program írja ki a szög mértéke 
alapján a szög típusát (pl.: 60 -> hegyesszög)! 
(http://www.altsuli.hu/matf/keretszogtip.html)
a.	véletlen számmal ugyanez
"""
)

# véletlen generálás
# csak jó értékekkel:
fok = random.randint(0,360)
# rossz értékekkel
fok = random.randint(-2,362)
print("A generált fok érték: ", fok)
if fok==0:
    print("Nullszög.")
elif fok>0 and fok<90:
    print("Hegyes szög.")
elif fok==90:
    print("Derékszög.")
elif fok>90 and fok<180:
    print("Tompa szög.")
elif fok==180:
    print("Egyenes szög.")
elif fok>180 and fok<360:
    print("Homorú szög.")
elif fok==360:
    print("Teljes szög.")
else:
    print("HIBA: Nem megfelelő szögérték!")