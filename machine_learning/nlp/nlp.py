# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:40:51 2019

@author: Yasko
"""

import numpy as np
import pandas as pd
import re

yorumlar = pd.read_csv('Restaurant_Reviews.csv')

yorum = re.sub('[^a-zA-Z]',' ',yorumlar['Review'][0])