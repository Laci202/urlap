class Pilota:

    def __init__(self,nev,szdatum,nemzetiseg,kod):
        self.nev=nev
        self.szdatum=szdatum
        daraboltDatum=szdatum.split("-")
        self.ev=int(daraboltDatum[0])
        self.honap = int(daraboltDatum[1])
        self.nap = int(daraboltDatum[2])
        self.nemzetiseg=nemzetiseg
        self.kod=kod

    def __str__(self):
        return "Név: {}, születési dátum: {}, nemzetiség: {}, kód: {}".format(self.nev,self.szdatum, self.nemzetiseg,self.kod)