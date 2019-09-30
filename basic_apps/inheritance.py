class Arac():
    def __init__(self,tur,model,marka):
        self.tur = tur
        self.model = model
        self.marka = marka
    def ozellikler(self):
        print("Türü:"+self.tur+"\n"+"Modeli:"+self.model+"\n"+"Marka:"+self.marka)

class Binek(Arac):
    def __init__(self,tur,model,marka,motor):
        super().__init__(tur,model,marka)
        self.motor = motor
    def ozellikler(self):
        super().ozellikler()
        print("Motor:"+self.motor)

class Ticari(Arac):
    def __init__(self,tur,model,marka,fiyat):
        super().__init__(tur,model,marka)
        self.fiyat = fiyat
    def ozellikler(self):
        super(Ticari, self).ozellikler()
        print("Fiyat:"+self.fiyat)

class Spor(Arac):
    def __init__(self,tur,model,marka,motor,hiz):
        super().__init__(tur,model,marka)
        self.motor = motor
        self.hiz = hiz
    def ozellikler(self):
        super(Spor, self).ozellikler()
        print("Motor:"+self.motor+"\n"+"Top Speed:"+self.hiz)

binek1 = Binek("Binek","2011","Honda","1.6 VTEC")
binek1.ozellikler()

