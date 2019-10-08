# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:20:39 2019

@author: Yasko
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from apyori import apriori

veriler = pd.read_csv('sepet.csv', header = None)

t = []
for i in range(0,7501):
    t.append([str(veriler.values[i,j]) for j in range(0,20)])


kurallar = apriori(t, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)
print(list(kurallar))

