import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
import scipy.io as si


for sub in range(1, 41):

    path1 = f"../projekat/Spectrogram temp/spect_temp_S{sub}_E1_A1.npy"
    path = f"../DB2/DB2_s{sub}/S{sub}_E1_A1.mat"
    # Učitavanje signala
    spectrogram = np.load(path1)
    a = si.loadmat(path)
    # spectrogram = np.transpose(a['emg'])
    labele = np.transpose(a['restimulus'])

    matrix = np.empty((129*3, 20*16))
    broj_pokreta = 0
    j = 0
    # print(len(spectrogram[0]))
    # plt.imshow(spectrogram)
    # plt.show()
    # svaki piksel zauzima po 640 samplova
    while j < len(labele[0]) and broj_pokreta < 102:

        while (labele[0, j] == 0):
            j = j + 1

        m = j // 128


        while (m + 16*5 >= len(spectrogram[0])):
            m = m-1

        mat_temp = spectrogram[:, m: m + 16*5]
        matrix[0:129, 0:5*16] = mat_temp[0:129]
        matrix[0:129, 5*16:10*16] = mat_temp[129:129*2]
        matrix[0:129, 10*16:15*16] = mat_temp[129*2:129*3]
        matrix[0:129, 15*16:20*16] = mat_temp[129*3:129*4]
        matrix[129:129*2, 0:5*16] = mat_temp[129*4:129*5]
        matrix[129:129*2, 5*16:10*16] = mat_temp[129*5:129*6]
        matrix[129:129*2, 10*16:15*16] = mat_temp[129*6:129*7]
        matrix[129:129*2, 15*16:20*16] = mat_temp[129*7:129*8]
        matrix[129*2:129*3, 0:5*16] = mat_temp[129*8:129*9]
        matrix[129*2:129*3, 5*16:10*16] = mat_temp[129*9:129*10]
        matrix[129*2:129*3, 10*16:15*16] = mat_temp[129*10:129*11]
        matrix[129*2:129*3, 15*16:20*16] = mat_temp[129*11:129*12]

        # plt.imshow(matrix)
        # plt.show()

        mov = broj_pokreta // 6 + 1
        pon = broj_pokreta % 6 + 1

        img_path = f"../projekat/Spectrogram hampel_noise1/{mov}/spect_hamp_noise1_S{sub}_E{sub}_Mov{mov}_Pon{pon}.npy"
        np.save(img_path, matrix)


        j=j+640*16

        if(j < len(labele[0])):
            while (labele[0, j] != 0):
                j = j + 1
                if (j == len(labele[0]) - 1):
                    break

        broj_pokreta = broj_pokreta + 1

    del spectrogram
    del mat_temp
    del labele

    # y = np.load(f"D:/projekat/Spectrogram Hampel/spect_hampel_S5_E5_Mov5_Pon5_Sli5.npy")
    # plt.imshow(y)
    # plt.show()