import requests
from bs4 import BeautifulSoup

url = "https://huseyindemirtas.net/ingilizce-ogrenmeye-nereden-baslamak-gerekir/"
tumkelimeler = []

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

def sembolleriTemizle(tumkelimeler):
    sembolsuzkelimeler = []
    semboller = "!'^+%&/()=?_-@\"*<>|[]{}.," + chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")
        if (len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler

for kelimegruplari in soup.find_all("p"):
    icerik = kelimegruplari.text
    kelimeler = icerik.lower().split()
    for kelime in kelimeler:
        tumkelimeler.append(kelime)

tumkelimeler = sembolleriTemizle(tumkelimeler)

frekans = []
for kelime in tumkelimeler:
    if kelime == "ingilizce":
        frekans.append(kelime)
print(len(frekans))