# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18IlMeZlPtlJt0_wgNsP0--IIprS5TGSH
"""

import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib notebook
import seaborn as sns
sns.set_style("darkgrid")

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print("Eğitim setinin boyutu: ")
print(train_images.shape)
print("Test setinin boyutu: " )
print(test_images.shape)

unique_classes, u_counts = np.unique(np.concatenate([train_labels, test_labels]), return_counts = True)
print("Unique class sayısı: ")
print(unique_classes)
print("Birim adet: ")
print(u_counts)

class_names = ['Tişört / Üst', 'Pantolon', 'Kazak', 'Elbise', 'Ceket',
               'Sandal', 'Gömlek', 'Spor Ayakkabı', 'Çanta', 'Çizme']

num_of_samples_per_class = 10
num_classes = len(unique_classes)

fig, axes = plt.subplots(nrows=num_classes, 
                         ncols=num_of_samples_per_class, 
                         figsize=(num_classes,num_of_samples_per_class))

for ix,current_class in enumerate(unique_classes):
    
    for iy,current_sample in enumerate(range(num_of_samples_per_class)):
    
        index = np.where([train_labels == current_class])[1][current_sample]
        
        current_image = train_images[index]
        
        axes[ix][iy].imshow(current_image, cmap=plt.cm.binary)
        axes[ix][iy].set_xticks([])
        axes[ix][iy].set_yticks([])

for ax, row in zip(axes[:,0], class_names):
    ax.set_title(row, rotation=0, size='large')

plt.subplots_adjust(hspace=0.5,wspace=0.2)

model = keras.Sequential([
                          keras.layers.Flatten(input_shape = (28, 28)),
                          keras.layers.Dense(128, activation='relu'),
                          keras.layers.Dense(10, activation='softmax')
])

model.count_params()

model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5) #Normalize etmeden eğitilen model ve accuracy değerleri çok düşük.

train_images = train_images / 255.0
test_images = test_images / 255.0
model.fit(train_images, train_labels, epochs=30) #Normalizasyon