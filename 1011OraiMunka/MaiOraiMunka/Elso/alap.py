print(
    """
    1.	A program olvasson be a konzolról egy egész 
    számot! A program döntse el, hogy a megadott szám 
    páros vagy páratlan, és írja ki az eredményt a 
    konzolra!
    """
)

szam=int(input("Kérem adjon meg egy egész számot!"))
if szam%2==0:
    print("Páros.")
else:
    print("Páratlan.")