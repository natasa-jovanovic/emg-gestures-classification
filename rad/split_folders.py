import splitfolders

audio_loc = '../projekat/Spectrogram hampel_noise1/'

splitfolders.ratio(audio_loc, output='../projekat/Spectrogram hampel_noise1/', seed=1337, ratio=(1, 0, 0))
