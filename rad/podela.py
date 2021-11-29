import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
import scipy.io as si


path1 = f"../projekat/Spectrogram notch_noise1/labele_train_spect_notch_noise1.npy"
# path2 = f"../projekat/Spectrogram notch_noise2/train_spect_notch_noise2.npy"
path3 = f"../projekat/Spectrogram notch1/labele_train_spect_notch1.npy"

fajl1 = np.load(path1)
# fajl2 = np.load(path2)
fajl3 = np.load(path3)

arr = fajl1.concatenate((fajl3))

np.save(f"../projekat/Spectrogram notch_noise_train/train_spect_notch_noise.npy", arr)