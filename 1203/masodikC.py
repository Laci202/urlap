print(
    """
    2.	Tölts fel egy listát 0-30-ig páros 
    számokkal (range)! Egy másikat 39-től 21-ig 
    páratlan számokkal!
    c.	Írasd ki a lista elemeit egy sorban, 
    minden 5. után sortöréssel!
    """
)
#kiíró eljárás
def kiir(lista):
    for index in range(0, len(lista),1):
        if((index+1)%5==0):
            print(lista[index])
        else:
            print(lista[index], end=" ")

    print("")

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

#c feladat
kiir(lista1)
kiir(lista2)