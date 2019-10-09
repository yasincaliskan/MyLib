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
import math

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

# UCB
N = 10000 # 10k tıklama
d = 10 # Toplam 10 ilan var
oduller = [0] * d # Başında bütün ilanların ödülü 0
tiklamalar = [0] * d # O ana kadarki tıklamalar
toplam = 0
secilenler = []

for n in range(0,N):
    ad = 0 # Seçilen ilan
    max_ucb = 0
    for i in range(0,d):
        if (tiklamalar[i] > 0):
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2* math.log(n)/tiklamalar[i])
            ucb = ortalama + delta
        else:
            ucb = N * 10
        if max_ucb < ucb:
            max_ucb = ucb
            ad = i
    
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = veriler.values[n, ad]
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul

print(toplam)
plt.hist(secilenler)
plt.show()








