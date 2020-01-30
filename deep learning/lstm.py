# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:26:55 2020

@author: Yasko
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
import matplotlib.patches as mpatches
from keras.layers.core import Dense,Activation,Dropout,Flatten,Reshape
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

data_orjinal = pd.read_csv('AirPassengers.csv')
data_orjinal = data_orjinal['#Passengers']

scaler = MinMaxScaler(feature_range=(0,1))
ts = scaler.fit_transform(data_orjinal.values.reshape(-1,1))
          
seed = 7
np.random.seed(seed)

timestep=3
X=[]
Y=[]

data = ts

for i in range(len(data)-timestep):
    X.append(data[i:i+timestep])
    Y.append(data[i+timestep])

X = np.asanyarray(X)
Y = np.asanyarray(Y)

X = X.reshape((X.shape[0],X.shape[1],1))


k = 70
Xtrain = X[:k,:,:]
Ytrain = Y[:k]

Xtest = X[k:,:,:]
Ytest = Y[k:]

model = Sequential()
model.add(LSTM(64,batch_input_shape=(None,timestep,1),return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32,return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1, activation='relu'))


model.compile(loss='mse',optimizer='rmsprop', metrics=['accuracy'])
model.fit(Xtrain, Ytrain, batch_size=512, epochs=50)

Ypred = model.predict(X)

Ypred = scaler.inverse_transform(Ypred)
Ypred = Ypred[:,0]

Yreel = data_orjinal[timestep:].values

plt.plot(Yreel,label='Yreel',color='blue')
plt.plot(Ypred,label='Ypred',color='red')

blue_patch = mpatches.Patch(color='blue', label='Yreel')
red_patch = mpatches.Patch(color='red', label='Ypred')
plt.legend(handles=[blue_patch,red_patch])
plt.title('RMSE: %.4f'% np.sqrt(sum((Ypred-Yreel)**2)/len(Yreel)))
plt.show()