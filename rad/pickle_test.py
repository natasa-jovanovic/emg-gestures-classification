import numpy as np
import os
import pickle

fajlovi = np.empty((45696, 50400))
filename = 'D:/projekat/Treniranje/1.Nonfiltered-windowing/fajlovi_train_p'
outfile = open(filename,'wb')

i = 0


for mov in range (1, 18):
    for filename in os.listdir(f"D:/projekat/Treniranje/1.Nonfiltered-windowing/train/{mov}/"):
        if filename.endswith(".npy"):
            path = os.path.join(f"D:/projekat/Treniranje/1.Nonfiltered-windowing/train/{mov}/", filename)
            fajl = np.load(path)
            f1D = fajl.flatten()
            fajlovi[i, :] = f1D
            i = i + 1
    print(mov)

pickle.dump(fajlovi, outfile)
outfile.close()

# np.save("D:/projekat/Treniranje/1.Nonfiltered-windowing/fajlovi_train.npy", fajlovi)