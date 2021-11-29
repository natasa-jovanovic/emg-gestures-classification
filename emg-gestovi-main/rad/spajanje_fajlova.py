import numpy as np
import os
import matplotlib.pyplot as plt

# fajlovi = np.empty((10030, 252*200))
fajlovi = np.empty((4080, 129*3*20*16))

i = 0

k=0
for mov in range (1, 18):
    for filename in os.listdir(f"../projekat/Spectrogram hampel_noise1/train/{mov}/"):
        if filename.endswith(".npy"):
            # 590 126
            path = os.path.join(f"../projekat/Spectrogram hampel_noise1/train/{mov}/", filename)
            fajl = np.load(path)
            f1D = fajl.flatten()
            fajlovi[i, 0:129*3*20*16] = f1D
            i = i+ 1
            k=k+1

    k=0
    print(mov)

# np.save("../projekat/Windowing notch/train_wind_notch10030.npy", fajlovi)
np.save("../projekat/Spectrogram hampel_noise1/train_spect_hamp_noise2.npy", fajlovi)

