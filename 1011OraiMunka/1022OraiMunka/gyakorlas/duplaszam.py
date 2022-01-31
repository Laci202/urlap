print(
    """
    1.	Duplaszam: Kérjen be a felhasználótól a konzolról 
    egy egész számot, és írja ki a képernyőre annak 
    kétszeresét! A megoldás tartalmazzon egy olyan eljárást, 
    amely paraméterként átveszi a beolvasott számot, és 
    saját maga számítja és írja ki annak kétszeresét!
    """
)
#eljárás
def ketszeres(szamom):
    ketszerese = szamom * 2
    print("A szám kétszerese: " + str(ketszerese))

szam=int(input("Kérem adjon meg egy egész számot!"))
ketszeres(szam)

