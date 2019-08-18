import sqlite3
import random
import time
import datetime


con = sqlite3.connect("dersler2.db")
cursor = con.cursor()

def tabloOlustur():
    cursor.execute('''CREATE TABLE IF NOT EXISTS talebeler(id integer, ad text, soyad text, numara integer, notu integer)''')
    con.commit()

def degerEkle():
    cursor.execute('''INSERT INTO talebeler VALUES (2,"baran","aydın",1412312,90)''')
    con.commit()


def tabloOlustur2():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tablo1(zaman REAL, tarih text, anahtarkelime text, deger real)''')
    con.commit()

def rastgeleDeger():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%y-%m-%d'))
    anahtarkelime = "python3sqlite"
    deger = random.randrange(0,10)
    cursor.execute('''INSERT INTO tablo1 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)''', (zaman,tarih,anahtarkelime,deger))
    con.commit()
tabloOlustur2()
i = 0
while (i < 10):
    rastgeleDeger()
    time.sleep(1)
    i += 1

con.close()
