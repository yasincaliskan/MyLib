# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:50:18 2019

@author: Yasko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,2:4].values

# KMeans
kmeans = KMeans(n_clusters=4, init='k-means++')
kmeans.fit(X)

print(kmeans.cluster_centers_) # Cluster noktalarını verir.

sonuclar = []
for i in range(1,10):     # Farklı cluster sayılarını dener.
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=100)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_) # WCSS değerlerini toplar.

plt.plot(range(1,10), sonuclar)









