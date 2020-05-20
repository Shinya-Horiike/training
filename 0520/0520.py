import numpy as np
from scipy.io import wavfile
import pyworld as pw

WAV_FILE = ("./data/vaiueo2d")

fs, data = wavfile.read(WAV_FILE+".wav")
data = data.astype(np.float) #WORLDはfloat前提らしい

_f0, t = pw.dio(data, fs)
f0 = pw.stonemask(data, _f0, t, fs)
sp = pw.cheaptrick(data, f0, t, fs)
ap = pw.d4c(data, f0, t, fs)

synthesized = pw.synthesize(f0, sp, ap, fs)

wavfile.write(WAV_FILE+"_conversion.wav", fs, synthesized)