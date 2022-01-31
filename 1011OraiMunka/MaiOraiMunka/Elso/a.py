import random
print(
    """
    1.	A program olvasson be a konzolról egy egész 
    számot! A program döntse el, hogy a megadott szám 
    páros vagy páratlan, és írja ki az eredményt a 
    konzolra!
    a.	Ugyanezt valósítsd meg véletlen számmal is!

    """
)
# szam = int(input("Kérem adjon meg egy egész számot!"))
szam = random.randint(-1000, 1000)
if szam % 2 == 0:
    print(szam,": Páros.")
else:
    print(szam, ": Páratlan.")
