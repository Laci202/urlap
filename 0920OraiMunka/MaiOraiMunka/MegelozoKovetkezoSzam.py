print(
    """
    A program kérjen be a konzolról egy egész
    számot! Ha a szám egyjegyű, akkor a program
    írja ki a konzolra a számot megelőző és
    követő egész számot, egyébként ne írjon
    ki semmit!
    """
)

szam=int(input("Kérem adjon meg egy egész számot!"))
if (szam<=9) and (szam>=-9):
    megelozo=szam-1
    kovetkezo=szam+1
    print("A számot megelöző és követő számok: "+str(megelozo)+", "+str(kovetkezo)+".")

