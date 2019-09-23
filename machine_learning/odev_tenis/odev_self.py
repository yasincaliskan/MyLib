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
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# Veri Yükleme

veriler = pd.read_csv('odev_tenis.csv')

# Encoding

le = LabelEncoder()
ohe = OneHotEncoder()

veriler2 = veriler.apply(LabelEncoder().fit_transform)
hava = veriler2.iloc[:,:1]
hava = ohe.fit_transform(hava).toarray()

play = veriler2.iloc[:,-1:].values
play[:,0] = le.fit_transform(play[:,0])
windy = veriler2.iloc[:,-2:-1].values
windy[:,0] = le.fit_transform(windy[:,0])

# DataFrame & Concat
4
hava = pd.DataFrame(data = hava, index = range(14), columns = ['overcast','rainy','sunny'])
sonveriler = pd.concat([hava, veriler.iloc[:,1:3]], axis=1)
sonveriler = pd.concat([veriler2.iloc[:,-2:], sonveriler], axis=1) 

# Verilerin train-test olarak bölünmesi

x_train, x_test, y_train, y_test = train_test_split(sonveriler.iloc[:,:-1], sonveriler.iloc[:,-1:], test_size = 0.33, random_state = 0)

# Linear Regression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

# Backward Elimination

X = np.append(arr = np.ones((14,1)).astype(int), values = sonveriler.iloc[:,:-1], axis=1)
X_l = sonveriler.iloc[:,[1,2,3,4,5]].values
r_ols = sm.OLS(endog = sonveriler.iloc[:,-1:], exog = X_l)
r = r_ols.fit()
print(r.summary())

x_train = x_train.iloc[:,1:]
x_test = x_test.iloc[:,1:]

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)












