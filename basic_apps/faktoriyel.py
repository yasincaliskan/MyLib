faktoriyel = 1
while(True):
    sayi = int(input("Bir sayı giriniz:"))
    if(sayi <= 0):
        print("Tekrar deneyin.")
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i
    break
print("sayının faktoriyeli:", faktoriyel)