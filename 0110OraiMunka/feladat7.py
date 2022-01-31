import renszarvas

lista=[]

def beolvas():
    #fájl elérése
    beFajlom=open("fileok/Mikulasszan.txt","r",encoding="utf-8")
    #első sor eldobása
    beFajlom.readline()
    #többi sor
    adatok=beFajlom.readlines()
    #print(adatok)
    #beolvasott sorok feldolgozása
    for sor in adatok:
        #sorvégejelektől megtisztítom
        sor=sor.strip()
        #eldarabolom
        darabolt=sor.split("@")
        #print(darabolt)
        #példányosítás
        szarvas=renszarvas.Renszarvaas(darabolt[0],darabolt[1],darabolt[2],darabolt[3])
        #print(szarvas)
        #listába fűzöm az objektumokat.
        lista.append(szarvas)

def kiir():
    #utasok kiírása
    for szarvas in lista:
        print(szarvas)


def mikulas():
    print(
"""
\tA feladathoz az adatokat a Mikulassszan.txt állományban találod. Ez egy rövid nyilvántartás, arról, hogy ki utazik a szánon.
\t1.	Olvasd be a mikulás rénszarvasainak adatait! 
\ta.	Írd ki a nevüket és a magasságukat.
\tb.	Hány rénszarvasa van a mikulásnak?
    c.	Írd ki Pompás idegen nyelvű megfelelőjét!
    d.	A rénszarvas leírásokban hányszor fordul elő a Mikulás szó?
    e.	Átlagosa milyen magasak a rénszarvasok?
    f.	Írd ki a páros helyen repülő szarvasok magyar nevét!
    g.	Hányadik rénszarvasnak a leghosszabb a kiírása? (Kinek a leírása áll a legtöbb karakterből?)
    h.	Ki repül a legkisebb sorszámú helyen?

        """
    )

    #szarvas1=renszarvas.Renszarvaas("Comet – Üstökös","140","2","A  Blorouis üstökös után kapta a nevét. Abban az időben ez vezette a csapatot a sötét és ködös éjszakán. Már az iskolában is kitűnő tanuló volt, a Mikulás igazi támaszának számított. Néha nagyon makacs, de erős. Különleges vezetői képességekkel rendelkezik, mindig a problémára összpontosít.")
    #print(szarvas1)
    beolvas()
    kiir()