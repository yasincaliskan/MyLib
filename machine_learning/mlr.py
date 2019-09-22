# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:20:50 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#1) Veri Önişleme
#1.1) Veri Yükleme
veriler = pd.read_csv('veriler.csv')

# ulke
ulke = veriler.iloc[:,0:1].values
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])

ohe  = OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

# cinsiyet
c = veriler.iloc[:,-1:].values
c[:,0] = le.fit_transform(c[:,0])

c = ohe.fit_transform(c).toarray()

# boy, kilo, yas

boy = veriler.iloc[:,1:2].values
kilo_yas = veriler.iloc[:,2:4].values


# Numpy dizilerinin DataFrame dönüşümü
sonuc = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])
sonuc2 = pd.DataFrame(data = boy, index = range(22), columns = ['boy'])
sonuc3 = pd.DataFrame(data = kilo_yas, index = range(22), columns = ['kilo', 'yas'])
sonuc4 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])

# DataFrame birleştirme
s = pd.concat([sonuc, sonuc2], axis=1)
s2 = pd.concat([sonuc3, sonuc4], axis=1)
s3 = pd.concat([s, s2], axis=1)

# boy için eğitim verisi
sol = s3.iloc[:,:3]
sag = s3.iloc[:,4:]

veri = pd.concat([sol, sag], axis=1)

# Verilerin train-test olarak bölünmesi
x_train, x_test, y_train, y_test = train_test_split(veri, boy, test_size = 0.33, random_state = 0)

# Verilerin ölçeklenmesi - Standartlaştırma

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

# Linear Regression - Model inşası
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)









