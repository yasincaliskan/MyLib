# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:20:50 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer, StandardScaler
from sklearn.model_selection import train_test_split


#1) Veri Önişleme
#1.1) Veri Yükleme
veriler = pd.read_csv('eksikveriler.csv')

#1.2) Eksik Veriler
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis=0)

Yas = veriler.iloc[:,1:4].values
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

# Encoder) Categoric -> Numeric
ulke = veriler.iloc[:,0:1].values

le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])

# OneHotEncoder -> Kolon başlıklarına etiketleri taşır
ohe = OneHotEncoder(categories='auto')
ulke = ohe.fit_transform(ulke).toarray()

# Numpy dizilerinin DataFrame dönüşümü
sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ['boy', 'kilo', 'yas'])

cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])

# DataFrame birleştirme
s1 = pd.concat([sonuc1, sonuc2], axis=1)
sonuc = pd.concat([s1, sonuc3], axis=1)

# Verilerin train-test olarak bölünmesi
x_train, x_test, y_train, y_test = train_test_split(s1, sonuc3, test_size = 0.33, random_state = 0)

# Verilerin ölçeklenmesi - Standartlaştırma
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)










