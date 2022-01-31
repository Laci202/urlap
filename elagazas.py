import math

#függvény
def beker(szoveg):
    szo=input(szoveg)
    return szo
#függvény
def kulonbseg(szo1,szo2):
    kulonbseg=math.fabs(len(szo1)-len(szo2))
    kulonbseg=int(kulonbseg)
    return kulonbseg

#eljárás
def hoszabb():
    # Írj egy metódust, mely a bekért 2 szöveg (szó) alapján eldönti, hogy melyik a hosszabb szó!
    szo1=beker("\tKérek egy szót: ")
    szo2=beker("\tKérek egy másik szót: ")
    #print(szo1,szo2)
    print("I/a.")
    #szavak hossza
    szo1hossz=len(szo1)
    szo2hossz=len(szo2)
    if szo1hossz>szo2hossz:
        print("\tA hosszabb szó: {}.".format(szo1))
    elif szo1hossz==szo2hossz:
        print("\tEgyenlő hosszúak.")
    else:
        print("\tA hosszabb szó: {}.".format(szo2))
    print("I/d.")
    kulonbsege=kulonbseg(szo1,szo2)
    print("\tA szavak hosszának a különbsége: {}".format(kulonbsege))


def elsoFeladat():
    hoszabb()