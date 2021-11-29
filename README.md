## Surface EMG signals classification for gesture recognition

Abstract

Recognition of hand movements based on surface EMG signal processing (sEMG) has become a promising approach for upper limb neuroprosthesis control.
The application of deep learning to sEMG data is a relatively new field of research aimed at finding adequate commercial prostheses that can enable movement
control. The goal of this project is to recognize the position and movements of the hand based on sEMG signals (the classification of data into 17 classes -
the number of movements and positions of the hand), using convolutional neural networks. It also investigates how the accuracy of classification is affected by
different types of signal preprocessing. Signals from the NinaPro database were used and they are processed in different ways. This database is intended to study
the relationship between surface electromyography, hand kinematics, and hand forces, with the ultimate goal of developing non-invasive, naturally controlled robotic
hand prostheses. The signals used are quite narrow in scope and therefore very sensitive to rough processing, as most of them transmit hand movement information that
is crucial for further classification. In addition to the noise that occurred due to the very nature of the movement of the hand and the movement of the signal
collection apparatus, the occurrence of noise in the vicinity of 50Hz was also expected, because of some characteristics of the used electrodes. The preprocessing
methods which are used are the Butterworth bandpass filter with bandwidth 30Hz-300Hz, bandstop Notch filter in the 50Hz frequency environment with Butterworth filter
30Hz-300Hz, and Hampel filter. The processed signals, as well as the raw data, were visualized by the spectrogram method. The spectrogram transmits the signal
strength using colors - the brighter the color, the higher the signal energy. By extracting the corresponding images from all 12 channels and merging them, one
image was obtained. Each spectrogram corresponds to one repetition of one movement. The formed images represent the input of the neural network. The training was
performed on all results and it was concluded that unfiltered signals give the best results of 86.9% validation accuracy. Signals pre-filtered with Butterworth
filter, Notch filter, and Hampel filter give results of 82.8%, 69.4%, and 84.5% validation accuracy respectively. For each training session, confusion matrices were
determined. From them, it can be noticed that the most commonly recognized movement is class 4, while the most commonly incorrectly determined movement is class 3.
Classes 14, 16, and 17 are most often misinterpreted, while a very small number of classes are mistakenly recognized as class 10. Spectrum The assumption that the
filtered signals will give the best results turned out to be wrong. This can also be attributed to the sensitivity of the signals themselves since the signal is mostly
modified by a combination of bandstop and bandpass filters. This is confirmed by the fact that the result of Hampel signals, which is the least changed, is a few
percent worse than the results of unfiltered signals.
