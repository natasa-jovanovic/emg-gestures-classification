import matplotlib.pyplot as plt
import scipy.io as si
import numpy as np
import pandas as pd

def hampel(vals_orig, k=7, t0=3):
    # Formiranje kopije
    vals = vals_orig.copy()
    # Hampel Filter
    L = 1.4826  # konstanta \sigma = 1.4826
    # Formiranje serije od niza
    s = pd.Series(vals)
    # rolling() funkcija koristi kotrljajuće prozore za računanje. Prosto rečeno, koristi se prozor veličine k
    # kroz vreme signala i primenjuju se neke željene matematičke operacije na njemu.
    rolling_median = s.rolling(k).median()  # median() - srednja rednost signala
    difference = np.abs(rolling_median - vals)
    s1=pd.Series(difference)
    median_abs_deviation = s1.rolling(k).median()
    threshold = t0 * L * median_abs_deviation # t0 - posmatraju se po 3 vrednosti sa obe strane trenutne
    outlier_idx = difference > threshold  # ako je razlika veća od granice vrednost postaje medijana
    vals[outlier_idx] = rolling_median[outlier_idx]
    return (vals)

for i in range(1, 2):
    path = f"../DB2/DB2_s{i}/S{i}_E1_A1.mat"
    # Učitavanje signala
    mat = si.loadmat(path)
    emg_signal = mat['emg']
    filt_signal=np.empty((len(emg_signal[:,0]), 12), dtype='float')
    for k in range(0,12):
        emg_el = emg_signal[:, k]
        output = hampel(emg_el,k=7,t0=3)
        filt_signal[:,k]=output
    filt_path = f"../projekat/Hampel signals/hampel_S{i}_E1.npy"
    np.save(filt_path, filt_signal)



# fs = 2000  # Frekvencija odabiranja
# t= np.arange(len(emg[:,0]))/fs  # Vreme

#  Kod za implementaciju Hampela bez Pandasa - predugo izvršavanje zbog ogromne petlje

# def hampel_filter(data, filtsize=6):
#
#     output = np.copy(np.asarray(data))
#     onesided_filt = filtsize // 2
#     for i in range(onesided_filt, len(data) - onesided_filt - 1):
#         dataslice = output[i - onesided_filt: i + onesided_filt]
#         mad = scipy.stats.median_abs_deviation(dataslice)
#         median = np.median(dataslice)
#         if output[i] > median + (3 * mad):
#             output[i] = median
#     return output
#
#
# mat = sc.loadmat('../DB2/DB2_s1/S1_E1_A1.mat')
# emg = mat['emg']
#
# fs = 2000  # Frekvencija odabiranja
# t= np.arange(len(emg[:,0]))/fs
#
# filtered = hampel_filter(emg[:,0], filtsize=6)

# fig = plt.figure()
# plt.plot(t, emg[:,0],'b')
# plt.plot(t, filtered,'r')
# plt.show()



