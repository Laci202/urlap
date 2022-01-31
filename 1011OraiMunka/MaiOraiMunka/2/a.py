#random csomag behívása
import random
print(
    """
    2.	A program  olvasson be a konzolról egy egész 
    számot! Ha a szám 1 és 12 közötti, akkor legyen a 
    beolvasott szám egy hónap sorszáma! A program írja 
    ki a konzolra a sorszámmal megadott hónap nevét! 
    Hiba (1-nél kisebb vagy 12-nél nagyobb szám) esetén 
    legyen hibaüzenet!
a.	Egy véletlen szám (1 és 12 között) alapján írasd ki 
az eredményt!

    """
)

#lecserélem a bekérést véletlen számos
#csak a jó értékek
szam=random.randint(1,12)
# randranggel ugyanez
# szam2=random.randrange(1,13)
#hibás értéket is generálok
#szam=random.randint(-300,1200)

print("A generált számérték: ", szam)
#eredeti program bemásolása
if szam>0 and szam<13:
    if szam==1:
        print("Január")
    elif szam==2:
        print("Február")
    elif szam==3:
        print("Március")
    elif szam==4:
        print("Április")
    elif szam==5:
        print("Május")
    elif szam==6:
        print("Június")
    elif szam==7:
        print("Július")
    elif szam==8:
        print("Agusztus")
    elif szam==9:
        print("Szeptember")
    elif szam==10:
        print("Október")
    elif szam==11:
        print("November")
    elif szam==12:
        print("December")
else:
    print("HIBA: A hónapok sorszáma csak 1-12 között "
          "lehet!")