def kokbul(a,b,c):
    delta = (b*b)-(4*a*c)
    if delta < 0:
        print("reel kök yok")
        return
    kok1 = (-b + delta ** 0.5)/(2*a)
    kok2 = (-b - delta ** 0.5) / (2 * a)
    return kok1, kok2

x = input("katsayıları giriniz:")
y = input("katsayıları giriniz:")
z = input("katsayıları giriniz:")

x1, x2 = kokbul(int(x),int(y),int(z))
print("1. kök:",x1,"2. kök:",x2)