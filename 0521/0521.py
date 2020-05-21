import numpy as np
from scipy.io import wavfile
import pyworld as pw

WAV_FILE = ("./data/vaiueo2d")

fs, data = wavfile.read(WAV_FILE+".wav")
data = data.astype(np.float) #WORLDはfloat前提らしい

f0, t = pw.harvest(data, fs)
#f0 = pw.stonemask(data, _f0, t, fs)
sp = pw.cheaptrick(data, f0, t, fs)
ap = pw.d4c(data, f0, t, fs)

conversion_f0 = f0*1.0  #数値を変えることでF0が変化
conversion_sp = np.zeros_like(sp)  
for f in range(conversion_sp.shape[1]):
    conversion_sp[:, f] = sp[:, int(f/1.0)]  #int内の分母の数値を変えることでSPが変化

synthesized = pw.synthesize(conversion_f0, conversion_sp, ap, fs)
synthesized = synthesized.astype(np.int16) #データ型を戻す必要あり

wavfile.write(WAV_FILE+"_conversion.wav", fs, synthesized)