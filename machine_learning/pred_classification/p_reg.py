# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:20:50 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Veri Önişleme
# Veri Yükleme
veriler = pd.read_csv('maaslar.csv')

# DataFrame (Slice)
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

# NumPy array dönüşümü
X = x.values
Y = y.values

# Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)



# Polynomial Regression
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

# 4. dereceden
poly_reg3 = PolynomialFeatures(degree=4)
x_poly3 = poly_reg3.fit_transform(X)

lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly3,y)

# Görselleştirme
plt.scatter(X,Y, color = 'blue')
plt.plot(x, lin_reg.predict(X), color = 'red')
plt.show()

plt.scatter(X,Y, color = 'blue')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = 'red')
plt.show()

plt.scatter(X,Y, color = 'blue')
plt.plot(X, lin_reg3.predict(poly_reg3.fit_transform(X)), color = 'red')
plt.show()







