import matplotlib.pyplot as plt
from scipy import signal
import scipy.io as si
import numpy as np


for sub in range(1, 41):
    # path1 = f"../projekat/Butterworth signals/butter_S{sub}_E1.npy"
    path = f"../DB2/DB2_s{sub}/S{sub}_E1_A1.mat"
    # Učitavanje signala
    mat = si.loadmat(path)
    emg_signal = np.transpose(mat['emg'])
    labele = np.transpose(mat['restimulus'])

    max = emg_signal.max()
    min = emg_signal.min()

    if min < 0:
        emg_signal = emg_signal + abs(min)
        diff = emg_signal.max()
    else:
        diff = max - min

    norm_signal = emg_signal / diff

    matrix = np.empty((252, 200))

    j = 0
    broj_pokreta = 0

    while j < len(labele[0]) and broj_pokreta < 102:

        while (labele[0, j] == 0):
            j = j + 1
            if (j == len(labele[0]) - 1):
                br = 16
                break

        br = 0
        while br < 16:
            k = 0
            m = j
            if (j + 600 > len(labele[0])):
                break

            for i in range(m, m + 420, 20):
                matrix[12 * k:12 * (k + 1), 0:200] = norm_signal[0:12, i:i + 200]
                k = k + 1
                j = j + 20

            mov = broj_pokreta // 6 + 1
            pon = broj_pokreta % 6 + 1
            img_path = f"../projekat/Windowing nonfiltered/{mov}/window_non_S{sub}_E{sub}_Mov{mov}_Pon{pon}_Sli{br+1}.npy"
            np.save(img_path, matrix)
            br = br + 1

        while (labele[0, j] != 0):
            j = j + 1
            if (j == len(labele[0]) - 1):
                break

        broj_pokreta = broj_pokreta + 1
        j = j + 1

    del mat
    del emg_signal
    del labele
    del norm_signal
    del matrix
