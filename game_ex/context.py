from game import *

e1 = Enemy()
p1 = Human()

while (e1.healt >= 0 or p1 >= 0):
    print("1) Punch \n 2) Kick")
    n = input("-->")
    p1.attack(n)

    e1.attack()