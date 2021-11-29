import matplotlib.pyplot as plt
from scipy import signal
import scipy.io as si
import scipy.io.wavfile
from scipy.signal import iirnotch
import numpy as np

def white_noise(n, mu=0):
    sigma = 0.00001 #0.000015
    noise = np.random.normal(mu, sigma, n)
    return noise

for i in range(1, 41):

    path = f"../DB2/DB2_s{i}/S{i}_E1_A1.mat"

    mat = si.loadmat(path)
    emg_signal = mat['emg']
    filt_signal=np.empty((len(emg_signal[:,0]), 12), dtype='float')
    for k in range(0,12):
        emg_el = emg_signal[:, k]
        fs = 2000
        fc = 50

        fl_n = 47.5
        fh_n = 52.5

        w = fc / (fs / 2)  # Normalizacija frekvencije
        Q = w / (fh_n - fl_n)

        b, a = iirnotch(w0=w, Q=Q, fs=fs)
        output_notch = signal.filtfilt(b, a, emg_el)

        fl = 30  # niza frekvencija bandpass filtera
        fh = 300  # visa frekvencija bandpass filtera

        wl = fl / (fs / 2)  # Normalizacija nize frekvencije
        wh = fh / (fs / 2)  # Normalizacija vise frekvencije
        b, a = signal.butter(5, [wl, wh], 'band')
        output_bandpass = signal.filtfilt(b, a, output_notch)
        # print(abs(output_bandpass).min())
        # print(abs(output_bandpass).max())
        # noise = np.random.normal(0, 1, len(output_bandpass))
        sr = 2000
        n = len(output_bandpass)
        noise = white_noise(n)
        signal_with_noise = output_bandpass + noise

        filt_signal[:,k]=signal_with_noise


    filt_path = f"../projekat/Notch signals/notch_noise1_S{i}_E1.npy"
    np.save(filt_path, filt_signal)
