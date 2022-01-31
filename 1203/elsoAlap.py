print(
    """
    1.	Kérj be 5 szót, majd minden elemét tedd egy 
    listába!
    """
)

#fügvények
def beker():
    szo=input("Kérem adjon meg egy szót!")
    return szo

#főprogram
#üres lista
lista=[]
for i in range(1,6,1):
    szo=beker()
    #új lista elem beszúrása a végére
    lista.append(szo)
#egész lista kiírása egybe
print(lista)

