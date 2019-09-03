import random

class Player():
    def __init__(self,race):
        self.race = race
        self.healt=100
        self.defense_point = random.randrange(5,10)
    def attack(self,attack_point):
        enemy.healt -= self.defense_point - self.attack_point
        return enemy.healt

class Human(Player):
    self.race ="Human"
    self.healt = 90

    def attack(self,attack_point,n):
        if(n == "1"):
            def punch():
                self.attack_point = 10
                return "Punch damage:" , attack_point
        elif(n == "2"):
            def kick():
                self.attack_point = 12
                return "Kick damage: " , attack_point
        else:
            pass

class Orcs(Player):
    self.race = "Orcs"
    self.healt = 110

    def attack(self,attack_point):
        if(n == "1"):
            def ax():
                self.attack_point = 12
                return "Ax damage:" + attack_point
        elif(n == "2"):
            def spear():
                self.attack_point = random.randrange(12,15)
                return "Spear damage:" + attack_point

            















"""class Dusman:
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

"""