import pandas as pd
import numpy as np
from keras.layers.core import Dense,Activation,Dropout,Flatten,Reshape
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

df = pd.read_excel(r'C:\Users\Yasko\Desktop\deep learning\numbers.xlsx')
print(df.shape)


raw_data = df.values

timestep = 5
X = []
Y = []

for i in range(len(raw_data)-(timestep)):
    X.append(raw_data[i:i+timestep])
    Y.append(raw_data[i+timestep])
    
X = np.asarray(X)
Y = np.asarray(Y)

X = X.reshape((X.shape[0], X.shape[1],1))

k = 2700 #eğitim verisi
Xtrain = X[:k,:,:]
Xtest = X[k:,:,:]

Ytrain = Y[:k]
Ytest = Y[k:]

model = Sequential()

model.add(LSTM(64, batch_input_shape=(None, timestep, 1),
               return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy'])


model.fit(Xtrain, Ytrain, batch_size=30,
          validation_data=(Xtest, Ytest),
          verbose = 1,
          epochs=50,
          shuffle=False)
