# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test =  X_test.reshape(10000, 784)

model = Sequential() #Sequential modeli oluşturuldu. Henüz içi boş.

#Katmanları eklemek için;
model.add(Dense(input_dim =  X_train.shape[1],
                output_dim =  50,
                init = 'uniform',
                activation =  'tanh'))
#Eklenen katman tipi Dense Layer: Tüm girişler ve tüm çıkışlar birbirine bağlı. Her birinin ayrı weighti var.
#Katmanları yerleştirirken her bir katmanın giriş boyutunun (input_dim), bir önceki katmanın çıkış boyutuna eşit olması gerekir.
#X_train.shape[1] değeri X_train matrisinde kaç kolon olduğunu (784) verir.
#init değişkeni başlangıçta katmanın içindeki weights nasıl sıfırlanacağını verir.
#Aktivasyon katmanların çıkışına takılan fonksiyonlardır. Ayrı bir aktivasyon katmanı olarak modele eklenebilir. 
#Her Keras katmanının bir activation özelliği vardır.

#Modele farklı katmanlar eklemek için;
from keras.layers.core import Activation, Dropout

model.add(Dense(50, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, init='uniform'))
model.add(Activation('relu'))

#Eklenen katmanlardan hiçbiri ilk katman olmadığı için input_dim vermeye gerek yok.
#Dropout weightlerin yarısını düşürür. Böylece overfitting engellenir.
#En son 64 çıkışlı Relu ile aktive olan katman eklendi.

#Bu 64 çıkışın 10 etikete (0'dan 9'a kadar) karşılık gelmesi için doğru değere karşılık gelenin 1
#diğer tüm çıkışların 0 olması gerekir. (one-hot-encoding)

#Bunun için yeni bir 10 çıkışlı Dense ekleyip aktivasyon fonksiyonu Softmax verilir.
model.add(Dense(10, init='uniform'))
model.add(Activation('softmax')) #64 çıkışın her birinin doğru rakamı bulabilmesi için.

#Çıkıştaki y_train vektörünün de one hot encoding formatına dönüşmesi gerekir.
#Bunun için Keras'ın to_categorical() fonksiyonu kullanılır.
from keras.utils.np_utils import to_categorical

y_train_ohe = to_categorical(y_train) #Model hazırlandı.

#Compile fonksiyonu ile modelin nasıl eğitileceği seçilmeli.
sgd = SGD(lr = 0.001, decay = 1e-6, momentum=0.9, nesterov = True)
#lr = learning rate = öğrenme hızı
#decay = öğrenme hızını zamanla azaltır.
#momentum ile bir hız vektörü tutulur ve her adımda update edilir.
#nesterov momentumu bunu daha akıllı yapar. Büyük bir adım attıktan sonra kendini düzeltir.

model.compile(loss = 'categorical_crossentropy', optimizer = sgd)
#categorical_crossentropy = Softmax ile kullanılan ve birden fazla sınıf için genelleştirilmiş lojistik regresyon.

model.fit(X_train, y_train_ohe, 
          nb_epoch = 50, 
          batch_size = 500, 
          validation_split = 0.1, 
          verbose = 1)

#batch_size = Her 500 örnekte bir adım atar.
#nb_epoch = Tüm veri setini 50 sefer yineler.
#validation_split = 60bin örneğin %90 kullanarak eğitir, %10 ile test eder ve hataları düzeltir.
#verbose = İşlem sırasında ekrana ayrıntılı bilgiler verir.

#Test setinden tahminler üretmek için;
y_test_predictions = model.predict_classes(X_test, verbose = 1)

#Tahminler oluştu. Doğruluğunu görmek için;
import numpy as np

correct = np.sum(y_test_predictions == y_test)
print('Test accuracy: ', correct/float(y_test.shape[0])*100.0, '%')
# %91.75 başarı elde edildi.

#Modeli görselleştirmek için;
"""
from keras.utils.visualize_util import plot
from IPython.display import Image
plot(model, to_file=’model.png’, show_shapes= True)
Image(“model.png”)
"""
# https://medium.com/turkce/keras-ile-derin-%C3%B6%C4%9Frenmeye-giri%C5%9F-40e13c249ea8



