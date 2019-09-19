# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:48:15 2019

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer

veriler = pd.read_csv('eksikveriler.csv')
print(veriler)

imputer = Imputer(missing_values='NaN', strategy = 'mean', axis=0)

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)


