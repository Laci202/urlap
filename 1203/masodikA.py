print(
    """
    2.	Tölts fel egy listát 0-30-ig páros 
    számokkal (range)! Egy másikat 39-től 21-ig 
    páratlan számokkal!
    a.	Fűzd egymás után a két listát az első 
    listában!
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
#listák ősszefűzés
lista1.extend(lista2)
print(lista1)
