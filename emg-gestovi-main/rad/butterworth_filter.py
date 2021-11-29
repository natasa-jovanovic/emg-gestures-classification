import matplotlib.pyplot as plt
from scipy import signal
import scipy.io as si
import numpy as np


for i in range(1,41):

    path = f"../DB2/DB2_s{i}/S{i}_E1_A1.mat"
    # Učitavanje signala
    mat = si.loadmat(path)
    emg_signal = mat['emg']
    filt_signal = np.empty((len(emg_signal[:, 0]), 12), dtype='float')
    for k in range(0,12):
        emg_el = emg_signal[:, k]

        fs = 2000  # Frekvencija odabiranja
        t = np.arange(len(emg_el)) / fs
        fc = 300  # Gornja granica propuštanja
        fc1 = 30  # Donja granica propuštanja

        # Normalizovanje
        w = fc / (fs / 2)
        w1 = fc1 / (fs / 2)

        # Formiranje butterworth band-pass filtera i njegova primena na signal
        b, a = signal.butter(7, [w1, w], btype='band')
        output = signal.filtfilt(b, a, emg_el)
        filt_signal[:, k] = output
    filt_path = f"../projekat/Butterworth signals/butter_S{i}_E1.npy"
    np.save(filt_path, filt_signal)

# Plotovanje sirovog i obrađenog signala
# plt.plot(t, emg[:,0], label='raw')
# plt.plot(t, output, label='filtered')
# plt.legend()
# plt.show()


# Frekvencijski i fazni odziv i njihov prikaz

# m, n = signal.freqz(b,a)
#
# fig = plt.figure()
# plt.title('Frequency response butterworth filter')
# plt.plot((m * fs)/ (2 * np.pi), 20 * np.log10(abs(n)), 'b')
# plt.ylabel('Amplitude [dB]', color='b')
# plt.xlabel('Frequency [Hz]')
#
#
# fig = plt.figure()
# plt.title('Phase response butterworth filter')
# angles = np.unwrap(np.angle(n))
# plt.plot((m * fs)/ (2 * np.pi), angles, 'g')
# plt.ylabel('Angle (radians)', color='g')
# plt.xlabel('Frequency [Hz]')
#
# plt.show()







