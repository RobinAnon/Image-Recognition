# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15t-TycNuYc13Xg_nUBiqkkh16ZYybEEF
"""

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline 
#car notebook

from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense, Dropout
#dropout limite l'overfitting 

from tensorflow.keras.models import Sequential

from tensorflow.keras.optimizers import Adam
#optimiser pour la backpropagation

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar10

INPUT_SHAPE = (32, 32, 3)
# width height channels
LR = 1e-4
#Learning rate
DECAY = 1e-6
BATCH_SIZE = 128
EPOCH = 250
#unité pour 1 parcours de dataset

VGG_CONVS = VGG16(weights='imagenet', include_top=False, input_shape=INPUT_SHAPE)
for layer in VGG_CONVS.layers:
  layer.trainable= False

model = Sequential([
    VGG_CONVS,
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.summary()

(X_train, Y_train), (X_valid, Y_valid) = cifar10.load_data()

size= X_train.shape[0] + X_valid.shape[0]
X_train.shape[0]/size

plt.figure(figsize=(19, 10))
plt.axis('off')

for x in range(4):
  for y in range(4):
    i= x + y*4
    img = X_train[i]
    
    plt.subplot(4, 4, i+1)
    plt.imshow(img)
plt.show()

Y_train[0]

labels = [
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck'
]

model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=LR, decay=DECAY), metrics=['accuracy'])

history = model.fit(X_train / 255.0 , to_categorical(Y_train), batch_size=BATCH_SIZE, shuffle=True, epochs=EPOCH, 
         validation_data=(X_valid/255.0, to_categorical(Y_valid)))

