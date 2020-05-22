import numpy as np
import soundfile as sf
import pyworld as pw

WAV_FILE = ("./data/vaiueo2d") 

data, fs = sf.read(WAV_FILE+".wav")

f0, t = pw.harvest(data, fs, 71.0, 800.0, 1.0)

option_cheaptrick_fft_size = 8192
sp = pw.cheaptrick(data, f0, t, fs, -0.15, 71.0, option_cheaptrick_fft_size)

option_d4c_fftsize = option_cheaptrick_fft_size
ap = pw.d4c(data, f0, t, fs, -0.15, option_d4c_fftsize)

Magnification_f0 = 2.0  #数値を変えることでF0が変化
ChangeValue_sp = 0 #数値を変えることでSPが変化

print( "F0 magnification = " + str(Magnification_f0) )  #F0の変換倍率の表示
print( "Spectram shift = " + str(ChangeValue_sp*(fs/2)/option_cheaptrick_fft_size) + " Hz" )  #スペクトル包絡のシフト量の表示

conversion_f0 = f0*Magnification_f0
conversion_sp = np.zeros_like(sp)
for f in range(conversion_sp.shape[1]):
    if f - ChangeValue_sp < 0:
        conversion_sp[:,f] = sp[:,1]
    elif f - ChangeValue_sp > conversion_sp.shape[1] -1:
        conversion_sp[:,f] = sp[:, conversion_sp.shape[1] -1]
    else:
        conversion_sp[:,f] = sp[:, f - ChangeValue_sp ]
 
synthesized = pw.synthesize(conversion_f0, conversion_sp, ap, fs, 1.0)

sf.write(WAV_FILE+"_conversion.wav", synthesized, fs)