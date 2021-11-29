import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
import scipy.io as si

def white_noise(n, mu=0):
    sigma = 0.00001 #0.000015
    noise = np.random.normal(mu, sigma, n)
    return noise

for sub in range(1, 41):


    path = f"../projekat/Hampel signals/hampel_S{sub}_E1.npy"
    # Učitavanje signala
    emg = np.load(path)
    samples = emg[:, 0]

    spectrum, freq, t, im = plt.specgram(samples, Fs=2000)

    x = len(spectrum[0])
    matrix = np.empty((1548, x))
    k=0

    for i in range(0, 12):

        samples1 = emg[:, i]
        n = len(samples1)
        noise = white_noise(n)
        samples = samples1 + noise

        spectrum, freq, t, im = plt.specgram(samples, Fs=2000)
        mat = im.get_array()

        matrix[129 * k:129 * (k + 1), :] = mat
        min = mat.min()
        max = mat.max()
        if min < 0:
            mat = mat + abs(min)
            diff = mat.max()
        else:
            diff = max - min

        norm_signal = mat / diff

        matrix[129 * k:129 * (k + 1), :] = norm_signal
        k=k+1

    # plt.imshow(matrix)
    # plt.show()
    img_path = f"../projekat/Spectrogram temp/spect_temp_S{sub}_E1_A1.npy"
    np.save(img_path, matrix)
