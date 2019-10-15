#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:03:45 2018

@author: sadievrenseker
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

# UCB
N = 10000 # 10k tıklama
d = 10 # Toplam 10 ilan var
oduller = [0] * d # Başında bütün ilanların ödülü 0
toplam = 0
secilenler = []
birler = [0] * d
sifirlar = [0] * d

for n in range(0,N):
    ad = 0 # Seçilen ilan
    max_th = 0
    for i in range(0,d):
        rasbeta = random.betavariate(birler[i] + 1, sifirlar[i] + 1)
        if rasbeta > max_th:
            max_th = rasbeta 
            ad = i
    secilenler.append(ad)
    odul = veriler.values[n, ad]
    if odul == 1:
        birler[ad] = birler[ad] + 1
    else:
        sifirlar[ad] = sifirlar[ad] + 1
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul

print(toplam)
plt.hist(secilenler)
plt.show()








