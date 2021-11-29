import numpy as np
import os

# labele= np.empty((10030, 1), int)
labele = np.empty((4080, 1), int)

# 612
i = 0

k=0
for mov in range (1, 18):
    for filename in os.listdir(f"../projekat/Spectrogram butterworth_noise1/train/{mov}/"):
        if filename.endswith(".npy"):
            # 590
            labele[i, 0] = mov-1
            i = i + 1
            k=k+1

    k=0
    print(mov)

np.save("../projekat/Spectrogram butterworth_noise1/labele_train_spect_butt_noise1.npy", labele)
# np.save("../projekat/Windowing notch/labele_test_wind_notch2142.npy", labele)



