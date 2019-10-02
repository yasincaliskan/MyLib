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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


#1) Veri Önişleme
#1.1) Veri Yükleme
veriler = pd.read_csv('veriler.csv')

x = veriler.iloc[5:,1:4].values
y = veriler.iloc[5:,4:].values

# Verilerin train-test olarak bölünmesi
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 0)

# Verilerin ölçeklenmesi - Standartlaştırma
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

# Logistic Regression
logr = LogisticRegression(random_state=0)
logr.fit(X_train, y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)

# Confusion Matrix (Karmaşıklık Matrisi)
cm = confusion_matrix(y_test, y_pred)
print(cm)
# Tahminin doğruluğunu gösteren matrisi verir.






























