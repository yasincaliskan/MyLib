# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:40:51 2019

@author: Yasko
"""

import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

yorumlar = pd.read_csv('Restaurant_Reviews.csv')

nltk.download('stopwords') # Stopwords indirildi.

ps = PorterStemmer() # Kelime gövdeleri / Stemmer

# Preprocessing
derlem = []
for i in range(1000):
    yorum = re.sub('[^a-zA-Z]',' ',yorumlar['Review'][i]) # Noktalama işaretlerini çıkarır.
    yorum = yorum.lower().split() # Küçük harfe çevirip listeye atar.
    yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words('english'))]
    yorum = ' '.join(yorum)
    derlem.append(yorum)

# Feature Extraction (Öznitelik çıkarımı) - Bag of Words
cv = CountVectorizer(max_features = 1000)
X = cv.fit_transform(derlem).toarray() # bağımsız değişken
y = yorumlar.iloc[:,1].values # bağımlı değişken

# Eğitim
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Gaussian Bayes Classification
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

# Confusion Matrix ile doğruluk
cm = confusion_matrix(y_test, y_pred)
print(cm) # %72.5 accuracy