# -*- coding: utf-8 -*-
"""mnist3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S20Xz1iOLLXv8YDORDeOK5O1sHVle8lR
"""

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD

from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

model = Sequential()

model.add(Dense(input_dim=X_train.shape[1],
                output_dim = 50,
                init =   'uniform',
                activation = 'tanh'))

from keras.layers.core import Activation
from keras.layers.core import Dropout

model.add(Dense(50, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, init='uniform'))
model.add(Activation('relu'))

from keras.utils.np_utils import to_categorical
y_train_ohe = to_categorical(y_train)

model.add(Dense(10, init='uniform'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss = 'categorical_crossentropy',
              optimizer = sgd,
              metrics=['accuracy'])

model.fit(X_train,
          y_train_ohe,
          nb_epoch = 10,
          batch_size = 500,
          validation_split = 0.1,
          verbose = 1)