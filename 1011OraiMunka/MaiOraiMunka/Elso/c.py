import random
import math
print(
    """
    1.	A program olvasson be a konzolról egy egész 
    számot! A program döntse el, hogy a megadott szám 
    páros vagy páratlan, és írja ki az eredményt a 
    konzolra!
    a.	Ugyanezt valósítsd meg véletlen számmal is!
    b.	Csak páros számot fogadj el, és add meg a 
    négyzetét!
    c.	Alakítsd át a b programot, hogy függvényel 
    működjön!

    """
)
#függvény
def parosEgesz():
    szam = random.randint(-1000, 1000)
    # db=1
    while not(szam%2==0):
        szam = random.randint(-1000, 1000)
    return szam


"""
szam = random.randint(-1000, 1000)
# db=1
while not(szam%2==0):
    szam = random.randint(-1000, 1000)
    # db+=1
    # print("db:"+str(db)+", szám: "+str(szam))
"""
szam2=parosEgesz()
negyzet= math.pow(szam2,2)
print("A véletlen szám("+str(szam2)+") négyzete: "+str(negyzet))
