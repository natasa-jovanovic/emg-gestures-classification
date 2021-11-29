import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
import scipy.io as si

emg = np.load('../rad/Hampel signals/hampel_S1_E1.npy')

samplerate = 2000
samples = emg[0:200,0]

spectrum, freq, t, im = plt.specgram(samples, Fs=samplerate)

mat = im.get_array()

min = mat.min()
max = mat.max()
if min < 0:
    mat = mat + abs(min)
    diff = mat.max()
else:
    diff = max - min

norm_signal = mat/diff

plt.show()