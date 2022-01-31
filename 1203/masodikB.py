import random
print(
    """
    2.	Tölts fel egy listát 0-30-ig páros 
    számokkal (range)! Egy másikat 39-től 21-ig 
    páratlan számokkal!
    b.	Minden 3. helyre illessz be egy 40 és 
    70 közötti véletlen számot!
    """
)
#üres lista
lista1=[]
#hozzáfűzöm az új lista elemeket
for elem in range(0,31,2):
    lista1.append(elem)
#ellenörzés
print(lista1)
#második lista
#üres lista
lista2=[]
for elem in range(39,20,-2):
    lista2.append(elem)
#ellenörzés
print(lista2)
#véletlen szám
vSzam=random.randint(41,69)
#beszúrás adott helyre adott értéket
lista1.insert(2,vSzam)
lista2.insert(2,vSzam)
#ellenörzés
print(lista1)
print(lista2)