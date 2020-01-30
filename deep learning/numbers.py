# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:39:31 2020

@author: Yasko
"""

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from keras.layers.core import Activation, Dropout
import numpy as np


train_data = [[1.0,2.0,3.0],[4.0,5.0,6.0]]
train_data_np = np.asarray(train_data)
train_label = [[1,2,3],[4,5,6]]
train_label_np = np.asarray(train_data)

# model.add(Dense(64, init='uniform'))

model = Sequential()

model.add(Dense(3, input_shape = (3, ))),
model.add(Dropout(0.2))
model.add(Dense(3, activation = 'sigmoid'))

#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss = 'categorical_crossentropy',
              optimizer = 'sgd',
              metrics=['accuracy'])


model.fit(train_data_np,
          train_label_np,
          epochs=10, 
          verbose=1)