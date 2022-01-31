import greenaway_o
lista=[]

def harmadikFeladat():
    #erőforrás beolvasása
    beFajl=open("greenaway.txt","r",encoding="utf-8")
    #első sor
    beFajl.readline()
    #többi sor
    adatok=beFajl.readlines()
    #print(adatok)
    #soronkénti feldolgozás
    for sor in adatok:
        #tisztítás
        tisztitottSor=sor.strip()
        #darabolás - mentén
        daraboltSor=tisztitottSor.split("-")
        #print(daraboltSor)
        #példánoysítok
        film=greenaway_o.Film(daraboltSor[0],daraboltSor[1])
        #végső listába példányok elhelyezése
        lista.append(film)

    #kiírás
    """
    for film in lista:
        print("A film címe:",film.cim, "éve:",film.ev)
    """

    print("III/b.")
    print("\tA filmek száma: {}.".format(len(lista)))
    print("III/d.")
    talalt=False
    for film in lista:
        if "szakács".lower() in film.cim.lower():
            talalt=True

    if talalt:
        print("\tVan olyan film amiben szerepel a \"szakács\" szó.")
    else:
        print("\tNincs olyan film amiben szerepel a \"szakács\" szó.")