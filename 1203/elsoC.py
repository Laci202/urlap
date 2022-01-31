print(
    """
    1.	Kérj be 5 szót, majd minden elemét tedd egy 
    listába!
    c.	Számold meg a “k” betűt tartalmazó szavakat!
    """
)

#fügvények
def beker():
    szo=input("Kérem adjon meg egy szót!")
    return szo

#főprogram
#üres lista
lista=[]
dbk=0
for i in range(1,6,1):
    szo=beker()
    #új lista elem beszúrása a végére
    #leellenörzöm, hoyg van-e benne k vagy K
    ciklusValtozo=0
    talaltK=True
    while(ciklusValtozo<len(szo) and talaltK):
        #print("beléptem")
        if szo[ciklusValtozo]=="k" or szo[ciklusValtozo]=="K":
            talaltK=False
            dbk+=1
        ciklusValtozo+=1

    lista.append(szo)
#egész lista kiírása egybe
print(lista)
print("A talált k betűs szavak száma:", dbk)

