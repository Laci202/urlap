"""
Írj programot, amely meghatározza, mennyi lesz
 egy betét értéke a futamidő végén,
ha 10000 Ft-t helyezünk betétbe 8%-os
névleges kamatláb mellett. Az évközi
kamatozások száma (m) 12. Az évek számát,
vagyis a t értékét a felhasználótól kérje
be a program.
segítő oldal: https://www.tantaki.hu/matek/kamatos_kamat
"""

t0=10000
p=0.08
"""n=12"""
n=int(input("Kérem adja meg az évek számát: "))
tn=t0*(pow(((100+p)/100),n))
#tn2=t0*(((100+p)/100)**n)
print("A kamatozott összeg: "+str(tn))
#print("A kamatozott összeg: "+str(tn2))


"""Hatványozás:
p1=pow(2,3)
p2=pow(3,4)
print(p1)
print(p2)
"""
