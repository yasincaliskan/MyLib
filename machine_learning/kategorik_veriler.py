# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:20:50 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer


veriler = pd.read_csv('eksikveriler.csv')

imputer = Imputer(missing_values='NaN', strategy = 'mean', axis=0)

Yas = veriler.iloc[:,1:4].values
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

ulke = veriler.iloc[:,0:1].values

le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])


ohe = OneHotEncoder(categories='auto')
ulke = ohe.fit_transform(ulke).toarray()


sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ['boy', 'kilo', 'yas'])

cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])

s1 = pd.concat([sonuc1, sonuc2], axis=1)
sonuc = pd.concat([s1, sonuc3], axis=1)
print(sonuc)