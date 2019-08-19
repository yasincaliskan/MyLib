class Dusman:
    def __init__(self):
        self.isim = "Düşman"
        self.can = 100
        self.saldiri = 5
        self.savunma = 5

    def round(self,player):
        def saldir(self,player):
            player.can -= self.saldiri - player.savunma

        def savunma(self,player):
            self.can -= player.saldiri - self.savunma

        while(self.can <= 0 or player.can <= 0):
            saldir(self,player)
            savunma(self,player)
            if(self.can == 0):
                print("Kazandın! Düşman öldü.")
                break
            elif(player.can == 0):
                print("Kaybettin! Düşman seni öldürdü.")
                break
            else:
                print("Düşmanın canı:", self.can, "\n", "Oyuncunun canı:", player.can)


class Insan:
    def __init__(self,isim=""):
        self.isim = isim
        self.can = 100
        self.saldiri = 7
        self.savunma = 3

class Ork:
    def __init__(self,isim=""):
        self.isim = isim
        self.can = 120
        self.saldiri = 5
        self.savunma = 5

class Buyucu:
    def __init__(self,isim=""):
        self.isim = isim
        self.can = 90
        self.saldiri = 8
        self.savunma = 4

