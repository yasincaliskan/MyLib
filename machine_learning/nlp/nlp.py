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

yorumlar = pd.read_csv('Restaurant_Reviews.csv')

# Noktalama işaretlerini çıkarır.
yorum = re.sub('[^a-zA-Z]',' ',yorumlar['Review'][0])

# Küçük harfe çevirip listeye atar.
yorum = yorum.lower().split()

# Stopwords indirildi.
nltk.download('stopwords')

# Kelime gövdeleri / Stemmer
ps = PorterStemmer()