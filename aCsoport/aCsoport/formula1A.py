import aCsoport.pilota

lista=[]
def beolvas():
    beFajl=open("aCsoport/drivers2.txt","r",encoding="utf-8")
    #beolvasás
    # első sor
    beFajl.readline()
    #többi sor
    adatok=beFajl.readlines()
    #feldologzás soronként
    for sor in adatok:
        #tiszítás
        tisztitottSor=sor.strip()
        #eldarabolni
        daraboltSor=tisztitottSor.split(";")
        #példányosítás
        pilotam=aCsoport.pilota.Pilota(daraboltSor[0],daraboltSor[1],daraboltSor[2],daraboltSor[3])
        #lista
        lista.append(pilotam)

def kiir():
    for pilota in lista:
        print(pilota)


def pilotakSzama():
    print("III/b:")
    print("\tA pilóták száma:",len(lista))

def januari():
    print("III/c:")
    print("\tJanuár 1-én születettek:")
    for pilota in lista:
        #print(str(pilota.honap)+","+str(pilota.nap))
        if pilota.honap==1 and pilota.nap==1:
            print("\t\t"+str(pilota.nev)+":"+str(pilota.szdatum))

def nemzetiseg():
    #megszámlálás tétel
    db=0
    for pilota in lista:
        if pilota.nemzetiseg=="Hungarian":
            db+=1

    print("III/d:")
    print("\tA magyar pilóták száma:"+str(db))
def pilotak():
    beolvas()
    #kiir()
    pilotakSzama()
    januari()
    nemzetiseg()