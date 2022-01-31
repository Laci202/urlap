print(
    """
    1.	Kérj be 5 szót, majd minden elemét tedd egy 
    listába!
    b.	Számold meg az 5 betűseket!
    körte, banán
    """
)

#fügvények
def beker():
    szo=input("Kérem adjon meg egy szót!")
    return szo

#főprogram
#üres lista
lista=[]
db=0
for i in range(1,6,1):
    szo=beker()
    hossz=len(szo)
    if hossz==5:
        db+=1
    #új lista elem beszúrása a végére
    lista.append(szo)
#egész lista kiírása egybe
print(lista)
print("Az ötbetűsök száma:",db)

