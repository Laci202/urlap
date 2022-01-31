print(
    """
3.	Osztályzat1: A program olvasson be a
konzolról egy egész számot! Ha a szám 0 és
100 közötti, akkor legyen a beolvasott szám
egy százalékérték! A program írja ki a konzolra
a százalékban megadott értékelést szövegesen 
(0%–59%-ig elégtelen, 60%–69%-ig elégséges, 
70%–79%-ig közepes, 80%–89%-ig jó, 90%–100%-ig
jeles)!
Ha a szám nem 0 és 100 közötti, akkor a program
írja ki a konzolra, hogy
„Hiba: érvénytelen százalék!”!
    """
)
szam=int(input("Kérem adjon meg egy egész számot!"))

if szam>=0 and szam<=100:
    if szam>=0 and szam<=59:
        print("Elégtelen.")
    elif szam>=60 and szam<=69:
        print("Elégséges.")
    elif szam>=70 and szam<=79:
        print("Közepes.")
    elif szam>=80 and szam<=89:
        print("Jó.")
    else:
        print("Jeles.")
else:
    print("Hiba: érvénytelen százalék!")
