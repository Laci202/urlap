print(
    """
    8.	Kérj be 2 szót (szöveget), és fűzd össze 
    őket úgy, hogy mindkét szó macskakörömmel 
    legyen kiíratva, de csak elöl és hátul (pl. 
    Be1: “alma”, Be2: “körte”, Ki: “alma körte”).
    """
)
#fügvények
def beker():
    szo=input("Kérem adjon meg egy szót!")
    return szo

def lecserel(szo):
    eredmeny=""
    for i in range(0,len(szo),1):
        if not(i==0 or i==(len(szo)-1)):
            eredmeny+=szo[i]
    return eredmeny
#főprogram
szo1 = beker()
szo2 = beker()
szo1l=lecserel(szo1)
szo2l=lecserel(szo2)

#eredmény kiírása
osszevont = "\""+str(szo1l)+" "+str(szo2l)+"\""
#osszevont2= "\"{} {}\"".format(szo1l,szo2l)
print(osszevont)