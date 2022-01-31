import random



def legkisebb(lista):
    print("II/b.")
    print("\t", end="")
    #minimum keresés listában
    minErtek=lista[0]
    minHely=0
    ciklusValtozo=1
    while ciklusValtozo<len(lista):
        if lista[ciklusValtozo]<minErtek:
            minErtek=lista[ciklusValtozo]
            minHely=ciklusValtozo
        ciklusValtozo+=1
    print("A legkisebb elem: {}.".format(minErtek))
    kiFajl=open("legkisebb.txt","w",encoding="utf-8")
    #print("\tA legkisebb elem: {}.".format(minErtek),file=kiFajl)
    kiFajl.write("\tA legkisebb elem: {}.".format(minErtek))
    kiFajl.close()

def kiir(lista):
    #print(lista)
    print("II/a.")
    print("\t",end="")
    for index in range(0,len(lista),1):
        if index==len(lista)-1:
            print(lista[index])
        else:
            print(str(lista[index])+"%",end="")

def listaFeltolt(hatar1,hatar2):
    lista = []
    #kisebb
    if hatar1<hatar2:
        min=hatar1
        max=hatar2
    else:
        min = hatar2
        max = hatar1

    # véletlen értékek előállítása
    # egy véletlen szám
    # szam=random.randint(100,200)
    # szam=random.randrange(100,201)
    # 13 db szám előállítása
    ciklusValtozo = 0
    while ciklusValtozo < 13:
        # egy véletlen szám
        szam = random.randint(min, max)
        # lista végére szúrás
        lista.append(szam)
        ciklusValtozo += 1
    # print(lista)
    return lista

def masodikFeladat():

    #lista elemeinek kiírása, a feltöltés értékeire
    adatok=listaFeltolt(100,200)
    kiir(adatok)
    legkisebb(adatok)
