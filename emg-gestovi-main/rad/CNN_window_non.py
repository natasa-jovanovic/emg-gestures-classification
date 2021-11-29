# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# import numpy as np
# import matplotlib.pyplot as plt
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.keras import datasets, layers, models
# import sklearn.metrics as metrics
# from numpy import loadtxt
# import keras
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.models import load_model


train_data = np.empty((45696, 7740))
i = 0
for mov in range (1, 18):
    for filename in os.listdir(f"D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/train/{mov}/"):
        if filename.endswith(".npy"):
            path = os.path.join(f"D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/train/{mov}/", filename)
            fajl = np.load(path)
            f1D = fajl.flatten()
            train_data[i, :] = f1D
            i = i + 1
    print(mov)


val_data = np.empty((9792, 7740))
i = 0
for mov in range (1, 18):
    for filename in os.listdir(f"D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/val/{mov}/"):
        if filename.endswith(".npy"):
            path = os.path.join(f"D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/val/{mov}/", filename)
            fajl = np.load(path)
            f1D = fajl.flatten()
            val_data[i, :] = f1D
            i = i + 1
    print(mov)


# test_data = np.load("D:/projekat/Treniranje/1.Nonfiltered-windowing/fajlovi_test.npy")
train_labels = np.load("D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/labele_train.npy")
val_labels = np.load("D:/projekat/Treniranje/5.Nonfiltered-spectrogram2/labele_val.npy")
# test_labels = np.load("D:/projekat/Treniranje/1.Nonfiltered-windowing/labele_test.npy")

class_names = ['Thumb up', 'Extension of index and middle finger, flexion of the others',
               'Flexion of ring and little finger, extension of the others',
               'Thumb opposing base of little finger', 'Abduction of all fingers',
               'Fingers flexed together in a fist', 'Pointing index', 'Adduction of extended fingers',
               'Wrist supination (axis: middle finger)', 'Wrist pronation (axis: middle finger)',
               'Wrist supination (axis: little finger)', 'Wrist pronation (axis: little finger)',
               'Wrist flexion', 'Wrist extension', 'Wrist radial deviation', 'Wrist ulnar deviation',
               'Wrist extension with closed hand']


# train_img.reshape(train_img.shape[0],1,129,60)

train_data=train_data.reshape((-1,129,60,1))
val_data=val_data.reshape((-1,129,60,1))

model = models.Sequential()
model.add(layers.Conv2D(40, (8, 3), activation='relu', input_shape=(129, 60, 1)))
model.add(layers.MaxPooling2D((2, 1)))

model.add(layers.Conv2D(40, (8, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 1)))

model.add(layers.Conv2D(40, (8, 3), activation='relu'))

model.add(layers.Conv2D(40, (8, 3), activation='relu'))

model.add(layers.Conv2D(40, (9, 3), activation='relu'))

model.add(layers.Flatten())

model.add(layers.Dense(400, activation='relu'))
model.add(layers.Dense(150, activation='relu'))
model.add(layers.Dense(17))
model.add(layers.Activation("softmax"))
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
model.summary()

es = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', mode = 'min',patience = 500, restore_best_weights = True)

history = model.fit(train_data, train_labels, epochs=10, validation_data=(val_data, val_labels))
model.save_weights('model.h5')