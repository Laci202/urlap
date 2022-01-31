print(
    """
     a.	Időtartam1A: Másodpercben megadott időtartamot 
     fejezzen ki óra:perc:másodperc formában! Ellenőrizni 
     nem kell! A megvalósítást egy külön eljárás végezze!   
    """
)

# adatbekérés
masodperc=int(input("Kérem adjon meg egy másodperc értéket!"))
while not(masodperc>=0):
    masodperc = int(input("Kérem adjon meg egy másodperc értéket!"))

#kiszámolás
percAtmeneti=masodperc/60
masodpercVegleges=int(masodperc%60)
oraVegleges=int(percAtmeneti/60)
percVegleges=int(percAtmeneti%60)

print(oraVegleges,":",percVegleges, ":", masodpercVegleges)


