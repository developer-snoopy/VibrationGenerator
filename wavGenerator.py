from isort import file
from matplotlib.colors import LinearSegmentedColormap
from scipy.io.wavfile import write
import numpy as np
import math

# Carrier Frequency: 100, 150, 200 Hz
# Amplitude: We should not use the amplitude as the parameter
# Duration: 50, 100, 300, 500, 1000, 2000 ms
# Envelope Frequency: 8, 16 Hz

sampling_rate = 44100;
carrier_freq = [100, 150, 200];
envelope_freq = [8, 16];
duration = [50, 100, 300, 500, 1000, 2000];

file_name = [];

def vibration_signal(i, j, k):
    t = np.linspace(0, duration[k], duration[k] * sampling_rate);
    signal = math.sin(2 * math.pi * carrier_freq[i] * t) * math.sin(2 * math.pi * envelope_freq[j] * t);
    return signal


for i in range (3):
    for j in range (2):
        for k in range (6):
            signal_name = str(carrier_freq[i]) + "Hz_" + str(envelope_freq[j]) + "Hz" + str(duration[k]) + "ms_";
            file_name.append(signal_name)
            write(signal_name + ".wav", sampling_rate, vibration_signal(i,j,k).astype(np.int16));

            print("The wav file is successfully saved - filename: " + file_name);