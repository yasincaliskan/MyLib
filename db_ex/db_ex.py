import sqlite3

con = sqlite3.connect("ornekdb.db")
cursor = con.cursor()


def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1(ad text,soyad text, numara int)")
    con.commit()

def veriEkle():
    a = str(input("ad:"))
    b = str(input("soyad:"))
    c = int(input("numara:"))
    cursor.execute("INSERT INTO tablo1 (ad,soyad,numara) VALUES(?,?,?)",(a,b,c))
    con.commit()

def tabloGoster():
    cursor.execute("SELECT * FROM tablo1")
    list = cursor.fetchall()
    for i in list:
        print(i)

def veriGoster():
    cursor.execute("SELECT * FROM tablo1 WHERE numara = 26")
    con.commit()

def veriGuncelle():
    cursor.execute("UPDATE tablo1 SET soyad= 'caliskan' WHERE numara = 26")
    con.commit()

def veriSil():
    cursor.execute("DELETE FROM tablo1 WHERE numara =1")
    con.commit()


veriSil()
tabloGoster()