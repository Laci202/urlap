print(
    """
4.	Osztályzat2: A program beolvas a konzolról 
egy egész számot! 
Ha a szám 1 és 5 közötti, akkor legyen a beolvasott
szám egy osztályzat! 
A program írja ki a konzolra a számmal megadott osztályzatot
szövegesen (1=elégtelen, …, 5=jeles)! 
Ha a szám nem 1 és 5 közötti, akkor a program írja ki
konzolra, hogy „érvénytelen osztályzat”!

    """
)
szam=int(input("Kérem adjon meg egy egész számot!"))
if szam>=1 and szam<=5:
    if szam==1:
        print("Elégtelen.")
    elif szam==2:
        print("Elégséges.")
    elif szam==3:
        print("Közepes.")
    elif szam==4:
        print("Jó.")
    else:
        print("Jeles.")
else:
    print("Érvénytelen osztályzat!")