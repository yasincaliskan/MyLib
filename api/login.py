defname = "yasko"
defpw = "1234"

while(True):
    name = input("kullanici adi:")
    pw = input("sifre:")

    if(defname == name) and (defpw == pw):
        print("başarılı giris")
        break
    elif(defname != name) and (defpw == pw):
        print("hatalı kullanıcı adı")
    elif(defname == name) and (defpw != pw):
        print("hatalı sifre! sifreyi değiştir(E/H):")
        ans = input()
        if(ans == "e"):
            defpw = input("yeni sifre:")
    else:
         print("tekrar deneyin")
         break
