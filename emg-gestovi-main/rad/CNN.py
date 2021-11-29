import os
import numpy as np
import matplotlib.pyplot as plt

# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class_names = ['Thumb up', 'Extension of index and middle finger, flexion of the others',
               'Flexion of ring and little finger, extension of the others',
               'Thumb opposing base of little finger', 'Abduction of all fingers',
               'Fingers flexed together in a fist', 'Pointing index', 'Adduction of extended fingers',
               'Wrist supination (axis: middle finger)', 'Wrist pronation (axis: middle finger)',
               'Wrist supination (axis: little finger)', 'Wrist pronation (axis: little finger)',
               'Wrist flexion', 'Wrist extension', 'Wrist radial deviation', 'Wrist ulnar deviation',
               'Wrist extension with closed hand']


def show_sample(sample, label):
    print(f"Sample shape {sample.shape}, Category: {class_names[label]}")
    plt.imshow(sample)
    plt.show()


def plot_performance(history, epochs):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()


def load_dataset(data_path, label_path, shape):
    labels = np.load(label_path)
    data = np.load(data_path).reshape((-1, *shape, 1))

    # randomize
    random_seq = np.random.permutation(len(data))
    return data[random_seq], labels[random_seq]


def train_spectrogram(epochs):
    x_train, y_train = load_dataset("D:/projekat/Treniranje/5.Nonfiltered-spectrogram/fajlovi5100_train_spec.npy", "D:/projekat/Treniranje/5.Nonfiltered-spectrogram/labele5000_train_spec.npy", shape=(129, 60))
    x_val, y_val = load_dataset("D:/projekat/Treniranje/5.Nonfiltered-spectrogram/fajlovi5100_val_spec.npy", "D:/projekat/Treniranje/5.Nonfiltered-spectrogram/labele5000_val_spec.npy", shape=(129, 60))

    show_sample(x_train[15], y_train[15][0])

    model = models.Sequential([
        layers.experimental.preprocessing.Rescaling(scale=2, offset=-1, input_shape=(129, 60, 1)),
        layers.Conv2D(40, (8, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 1)),
        layers.Conv2D(40, (8, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 1)),
        layers.Conv2D(40, (8, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(40, (8, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(40, (9, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Flatten(),
        layers.Dense(200, activation='relu'),
        layers.Dense(150, activation='relu'),
        layers.Dense(17),
        layers.Activation("softmax")
    ])

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), metrics=['accuracy'])
    model.summary()

    kill_switch = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', patience=500, restore_best_weights=True)

    history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val, y_val), callbacks=[kill_switch])

    plot_performance(history, epochs)
    # model.save_weights('model.h5')


if __name__ == "__main__":
    train_spectrogram(epochs=20)
