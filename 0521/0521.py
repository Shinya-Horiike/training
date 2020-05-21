import numpy as np
from scipy.io import wavfile
import pyworld as pw

WAV_FILE = ("./data/vaiueo2d") #24bit非対応

fs, data = wavfile.read(WAV_FILE+".wav")
data = data.astype(np.float) #WORLDはfloat前提らしい

f0, t = pw.harvest(data, fs)

option_cheaptrick_fft_size = 8192
option_d4c_fftsize = option_cheaptrick_fft_size

sp = pw.cheaptrick(data, f0, t, fs, -0.15, 71.0, option_cheaptrick_fft_size)
ap = pw.d4c(data, f0, t, fs, -0.15, option_d4c_fftsize)

conversion_f0 = f0*1.0  #数値を変えることでF0が変化
ChangeValue_sp = 0 #数値を変えることでSPが変化

conversion_sp = np.zeros_like(sp)
for f in range(conversion_sp.shape[1]):
    if f - ChangeValue_sp < 0:
        conversion_sp[:,f] = sp[:,1]
    elif f - ChangeValue_sp > conversion_sp.shape[1] -1:
        conversion_sp[:,f] = sp[:, conversion_sp.shape[1] -1]
    else:
        conversion_sp[:,f] = sp[:, f - ChangeValue_sp ]
 
synthesized = pw.synthesize(conversion_f0, conversion_sp, ap, fs)
synthesized = synthesized.astype(np.int16) #データ型を戻す必要あり

wavfile.write(WAV_FILE+"_conversion.wav", fs, synthesized)