# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:20:50 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import statsmodels.api as sm


# Veri Önişleme
# Veri Yükleme
veriler = pd.read_csv('maaslar_yeni.csv')

# DataFrame (Slice)
x = veriler.iloc[:,2:5]
y = veriler.iloc[:,5:]

X = x.values
Y = y.values

print(veriler.corr())

# Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)
print("Linear Regression R2: ", r2_score(Y,lin_reg.predict(X)))

# P-Value
print("Linear OLS")
model = sm.OLS(lin_reg.predict(X),X)
print(model.fit().summary())

# Polynomial Regression
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
print("Polynomial Regression R2: ", r2_score(Y,lin_reg2.predict(poly_reg.fit_transform(X))))

print("Poly OLS")
model2 = sm.OLS(lin_reg2.predict(poly_reg.fit_transform(X)),X)
print(model2.fit().summary())

# 4. dereceden
poly_reg3 = PolynomialFeatures(degree=4)
x_poly3 = poly_reg3.fit_transform(X)

lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly3,y)

# Verilerin ölçeklenmesi - Standartlaştırma
sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

# Support Vector Regression
svr_reg = SVR(kernel = 'rbf')
svr_reg.fit(x_olcekli, y_olcekli)

print("SVR R2: ", r2_score(y_olcekli,svr_reg.predict(x_olcekli)))

print("SVR OLS")
model3 = sm.OLS(svr_reg.predict(x_olcekli),x_olcekli)
print(model3.fit().summary())

# Decision Tree
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)

print("Decision Tree R2: ", r2_score(Y,r_dt.predict(X)))
print("DT OLS")
model4 = sm.OLS(r_dt.predict(X),X)
print(model4.fit().summary())

# Random Forest Regression
rf_reg= RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X,Y)

print("Random Forest OLS")
model5 = sm.OLS(rf_reg.predict(X),X)
print(model5.fit().summary())

# R2 Score
print("Random Forest R2: ", r2_score(Y,rf_reg.predict(X)))
























