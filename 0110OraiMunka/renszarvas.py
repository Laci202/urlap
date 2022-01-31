class Renszarvaas():

    #konsturktor: változók kezdeti érétkeinek beállítása
    def __init__(self, nev, magassag, hely, leiras):
        #Mikulás
        if magassag=="nem ismert":
            #Mikulásról van szó
            self.magassag=0
        else:
            self.magassag=int(magassag)
        self.leiras=leiras
        self.hely=int(hely)
        #szétbontjuk
        bontott=nev.split(" – ")
        #print(bontott)
        self.angolNev=bontott[0]
        self.magyarNev=bontott[1]

    def __str__(self):
        return "Angolnév: {}, magyarnév: {}, magassag: {}, hely: {}, leírás: {}".format(self.angolNev,self.magyarNev,self.magassag, self.hely, self.leiras)