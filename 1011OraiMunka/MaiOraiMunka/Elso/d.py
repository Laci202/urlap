import math
import paros
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
szam2 = paros.parosEgesz()
negyzet = math.pow(szam2, 2)
print("A véletlen szám("+str(szam2)+") négyzete: "+str(negyzet))
