while True:
    a = int(input("1. Sayı:"))
    b = int(input("2. Sayı:"))

    def topla(a,b):
        sonuc = a + b
        return sonuc
    def cikar(a,b):
        sonuc = a - b
        return sonuc
    def bol(a,b):
        sonuc = a / b
        return sonuc
    def carp(a,b):
        sonuc = a * b
        return sonuc

    c = str(input("Hangi İşlem? 1/2/3/4: "))

    if (c == "1"):
        sc = topla(a,b)
        print(sc)
    elif (c == "2"):
        sc = cikar(a,b)
        print(sc)
    elif (c == "3"):
        sc = bol(a,b)
        print(sc)
    elif (c == "4"):
        sc = carp(a,b)
        print(sc)
    else:
        print("hatalı giris!")
    continue
