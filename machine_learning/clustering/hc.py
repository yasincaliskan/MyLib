# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:50:18 2019

@author: Yasko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,2:4].values

# KMeans
kmeans = KMeans(n_clusters=4, init='k-means++')
kmeans.fit(X)

print(kmeans.cluster_centers_) # Cluster noktalarını verir.

sonuclar = []
for i in range(1,11):     # Farklı cluster sayılarını dener.
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=100)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_) # WCSS değerlerini toplar.

plt.plot(range(1,11), sonuclar)
plt.show()

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=100)
Y_tahmin = kmeans.fit_predict(X)

plt.scatter(X[Y_tahmin==0,0], X[Y_tahmin==0,1], s=100, color='red')
plt.scatter(X[Y_tahmin==1,0], X[Y_tahmin==1,1], s=100, color='blue')
plt.scatter(X[Y_tahmin==2,0], X[Y_tahmin==2,1], s=100, color='green')
plt.scatter(X[Y_tahmin==3,0], X[Y_tahmin==3,1], s=100, color='yellow')
plt.title('KMeans')
plt.show()

# HC
ac = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
Y_tahmin = ac.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0], X[Y_tahmin==0,1], s=100, color='red')
plt.scatter(X[Y_tahmin==1,0], X[Y_tahmin==1,1], s=100, color='blue')
plt.scatter(X[Y_tahmin==2,0], X[Y_tahmin==2,1], s=100, color='green')
plt.scatter(X[Y_tahmin==3,0], X[Y_tahmin==3,1], s=100, color='yellow')
plt.title('HC')
plt.show()

# Dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()







