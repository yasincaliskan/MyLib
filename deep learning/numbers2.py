# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:39:31 2020

@author: Yasko
"""

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
import numpy as np



train_data = [[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]]
train_data_np = np.asarray(train_data)
train_label = [["birler"],["onlar"]]
train_label_np = np.asarray(train_data)

print(train_data_np.shape)
print(train_label_np.shape)

#model.add(Dense(64, init='uniform'))

model = Sequential()

model.add(Dense(10, input_shape = (10, ))),
model.add(Dropout(0.2))
model.add(Dense(10, activation = 'sigmoid'))
"""model.add(Dropout(0.2))
model.add(Dense(3, activation = 'relu'))"""

#sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss = 'categorical_crossentropy',
              optimizer = 'sgd',
              metrics=['accuracy'])

model.fit(train_data_np,
          train_label_np,
          batch_size=5,
          epochs=10, 
          verbose=1)

tahmin = []
tahminarray = []

for i in range(10,20):
    tahmin.append(i)
tahminarray.append(tahmin)
tahmin_np = np.asarray(tahminarray)
#print(tahminarray)

results = model.predict(tahmin_np)
print(results)