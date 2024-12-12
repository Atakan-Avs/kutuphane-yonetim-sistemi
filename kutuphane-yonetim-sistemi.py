class Kitap:
    def __init__(self,kitapBasligi,yazar,mevcut=True):
        self.kitapBasligi=kitapBasligi
        self.yazar=yazar
        self.mevcut=mevcut
    def oduncAl(self):
        if self.mevcut:
            self.mevcut=False
            print(f"{self.kitapBasligi} ödünç alındı")
        else:
            print(f"{self.kitapBasligi} zaten ödünçte")
    def iadeEt(self):
        self.mevcut=True
        return (f"{self.kitapBasligi} iade edildi")
    
class Kütüphane:
    def __init__(self):
        self.kitaplar=[]
    def kitapEkle(self,kitap):
        self.kitaplar.append(kitap)
    def kitapGoster(self):
        for kitap in self.kitaplar:
            durum="mevcut" if kitap.mevcut else "ödünçte"
            print(f"{kitap.kitapBasligi} - {kitap.yazar} - {durum}")

kutuphane=Kütüphane()
kitap1=Kitap("Satranç","Stefan Zweig")
kitap2=Kitap("Ay Işığı Sokağı","Stefan Zweig")

kutuphane.kitapEkle(kitap1)
kutuphane.kitapEkle(kitap2)

kutuphane.kitapGoster()
kitap1.oduncAl()
kutuphane.kitapGoster()
kitap1.iadeEt()
