import oyun

dusman = oyun.Dusman()
player = oyun.Buyucu()
player.isim = "Yasko"
print(player.isim)

oyun.Dusman.round(dusman,player)
