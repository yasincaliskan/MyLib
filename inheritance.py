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

binek1 = Binek("Binek","2017","Honda","1.6 VTEC")
binek1.ozellikler()

ticari1 = Ticari("Ticari","2011","Fiat","40.000 TL")
ticari1.ozellikler()