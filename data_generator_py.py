# -*- coding: utf-8 -*-
"""Data_Generator.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cS2usPq0jz2z2aqdLPlHyAsF4MagqCy-
"""

!wget https://www.dropbox.com/s/ie7h1hob7uhuf5v/archive.zip?dl=0

!unzip archive.zip?dl=0

!ls

import os
folder = os.listdir("dataset")
folder.remove('dataset')
folder

for f in folder:
  path = "dataset/"+f
  print(f+" "+str(len(os.listdir(path))))

from keras.preprocessing.image import image
from matplotlib import pyplot as plt

sample_path = "dataset/cats/cat.1.jpg"
img = image.load_img(sample_path)
img = image.img_to_array(img)/255.0

print(type(img))

plt.imshow(img)
plt.axis("off")
plt.show()

from keras.layers import *
from keras.models import Sequential

model = Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(128,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(128,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D((2,2)))
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dense(4,activation='softmax'))
model.summary()

from keras.optimizer_v2.adam import Adam
adam = Adam(lr = 1e-4)

model.compile(loss="categorical_crossentropy",optimizer = adam,metrics=["accuracy"])

# model.fit()   this method we use when our data is small and can be fit inside memory 
# so instead of this we use generator which can load a single batch at a time and load that single batch inside memory

from keras.preprocessing.image import ImageDataGenerator

train_gen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_gen.flow_from_directory(
    "dataset/",
    target_size = (150,150),
    batch_size = 32,
    class_mode = "categorical"
)

train_generator.labels

# this will return next batch
x,y = train_generator.next()
print(x.shape,y.shape)

# we can also itrate over generator to get batch
for x,y in train_generator:
  print(x.shape,y.shape)
  break;

history = model.fit_generator(
    train_generator,
    epochs = 20,
    steps_per_epoch=7,
)

