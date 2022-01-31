print(
    """
    1.	Kérj be 5 szót, majd minden elemét tedd egy 
    listába!
    a.	Add meg a leghosszabb szó hosszát!
    """
)

#fügvények
def beker():
    szo=input("Kérem adjon meg egy szót!")
    return szo

#főprogram
#üres lista
lista=[]
leghoszabb=""
leghoszabbHossza=0
db=0
leghoszabbHely=0
for i in range(1,6,1):
    szo=beker()
    db+=1
    hossz=len(szo)
    if hossz>leghoszabbHossza:
        leghoszabb=szo
        leghoszabbHossza=len(szo)
        leghoszabbHely=db

    #új lista elem beszúrása a végére
    lista.append(szo)
#egész lista kiírása egybe
print(lista)
print("A leghoszabb szavam:",leghoszabb, "ezen a helyen taláálható: ",leghoszabbHely)

