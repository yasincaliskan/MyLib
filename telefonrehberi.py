list = []
while True:
    a = int(input("Rehber\n 1)Kişiler\n 2)Kişi Ekle\n 3)Çık\n -->"))
    if (a == 1):
        dosya = open("rehber.txt","r")
        list = dosya.read()
        dosya.close()
        print(list)
    elif (a == 2):
        y = (input("Numarayı giriniz:"))
        x = (input("İsim giriniz:"))
        z = {x:y}
        list.append(z)
        dosya = open("rehber.txt","w")
        dosya.write(str(list))
        dosya.close()
    elif (a == 3):
        print("Rehber kapanıyor..")
        break