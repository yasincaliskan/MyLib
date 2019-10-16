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
import statsmodels.formula.api as sm


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

# Backward Elimination
X = np.append(arr = np.ones((22,1)).astype(int), values = veri, axis=1)    
X_l = veri.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(endog = boy, exog = X_l).fit()
print(r_ols.summary())

X_l = veri.iloc[:,[0,1,2,3,5]].values
r_ols = sm.OLS(endog = boy, exog = X_l).fit()
print(r_ols.summary())

X_l = veri.iloc[:,[0,1,2,3]].values
r_ols = sm.OLS(endog = boy, exog = X_l).fit()
print(r_ols.summary())

# Verilerin train-test olarak bölünmesi
x_train, x_test, y_train, y_test = train_test_split(veri, boy, test_size = 0.33, random_state = 0)

# Linear Regression - Model inşası
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)







