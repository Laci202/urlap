
import random
def beker(szoveg):
    szo=input(szoveg)
    return szo
"""
def random(szoveg):
    szo=beker("kérek egyet")
    osszesen=0
    for i in range(0,szo):
        osszesen=osszesen+i
    return osszesen

szam=beker("Kérek egy természetes számot")
osszeg=0
for i in range(1,int(szam)+1):
    osszeg=osszeg+i
    #print(i)
print(osszeg)

szam1=int(beker("Kérek egy számot"))#faktorális
n=1
if szam1 >= 0:
    for i in range(1,szam1+1):
        n=n*i
        print(i)
    print(str(i)+"faktorális"+str(n))
else:
    print("nem mefelelő")

szam2=int(beker("Kérek egy természetes számot"))
osszeg=0
for i in range(1,szam2+1):
    osszeg=osszeg+i
    #print(i)
print(osszeg/szam2)

primszam=True
szam3=int(beker("kérek egy számot"))
for i in range(2,szam3):
    print(szam3 % i)
    if (szam3 % i) != 0:
        primszam=False
print(primszam)
if primszam:
    print("primszam")
else:
    print("nem primszám")

szam4=int(beker("Kérek egy természetes számot"))
if szam4 % 2 :
    print("nem páros")
else:
    print("páros")

file=open("legkisebb.txt", "r")
a=str(len(file.read()))
print(a)

file1=open("kiSzovegDB.txt", "w")
file1.write(a)
file.close()
file1.close()

szam4=beker("Kérek egy természetes számot")
print(str(len(szam4)))
"""
szam1=int(beker("bekér kisseb szám"))
szam2=int(beker("bekér nagyobb szám"))
db=0

for i in range(szam1,szam2+1):
    if i % 2:
        db+=1
print(db)

db=0

a=random.randint(-5,5)
b=random.randint(-5,5)
print(a)
print(b)
if a > b:
    for i in range(b,a):
            if i % 2:
                db+=1
else:
     for i in range(a,b):
            if i % 2:
                db+=1
print(db)
