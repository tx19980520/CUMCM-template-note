# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:50:45 2018

@author: ty020
"""

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 255.0
train_images = np.expand_dims(train_images, axis= 4)

test_images = test_images / 255.0
test_images = np.expand_dims(test_images, axis= 4)

model = tf.keras.Sequential([
    keras.layers.Conv2D(data_format="channels_last",filters = 1,activation=tf.nn.relu, kernel_size = 5, strides=[ 1, 1], padding="same",input_shape=(28, 28, 1)),
    keras.layers.MaxPool2D(pool_size=[3, 3]),
    keras.layers.Flatten(input_shape=(10, 10)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=20)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)