from isort import file
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt



def vibrationGenerator(sampling_rate, carrier_freq, envelope_freq, duration):
    import numpy as np

    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint = False)

    if envelope_freq != 0:
        signal = np.sin(2 * np.pi * envelope_freq * t) * np.sin(2 * np.pi * carrier_freq *  t)
    else:
        signal = np.sin(2 * np.pi * carrier_freq * t)
    return signal, t

# Carrier Frequency: 100, 150, 200 Hz
# Amplitude: We should not use the amplitude as the parameter
# Duration: 50, 100, 300, 500, 1000, 2000 ms
# Envelope Frequency: 8, 16 Hz

sampling_rate = 10000;
carrier_freq = [100, 150, 200];
envelope_freq = [8, 16];
amplitude = np.iinfo(np.int16).max;
duration = [0.05, 0.3, 2];

file_name = [];
signal_set = [];

for d in duration:
    for e in envelope_freq:
        for c in carrier_freq:
            signal_name = "carrier" + str(c) + "Hz_" + "envelop" + str(e) + "Hz_" + "duration" + str(d) + "sec";
            # print(signal_name)
            
            write(signal_name + ".wav", sampling_rate, vibrationGenerator(sampling_rate, c, e, d)[0]);
            print("Completely saved as " + signal_name);

            signal_temp, t_temp = vibrationGenerator(sampling_rate, c, e, d)
            signal_set.append([signal_temp, t_temp, c, e, d])


plt.figure(figsize = (20,30))

for i in range (0, len(signal_set)):
    plt.subplot(len(signal_set), 1, i + 1)
    plt.plot(signal_set[i][1], signal_set[i][0])
    plt.title('Carrier Frequency: {}Hz, Envelope Frequency: {}Hz, Duration: {}s'.format(signal_set[i][2], signal_set[i][3], signal_set[i][4]))
    plt.xlabel('time(sec)')
    plt.ylabel('G')

plt.rc('font', size = 23)
plt.tight_layout()
plt.show()



# for i in range (3):
#     for j in range (2):
#         for k in range (6):

            
#             signal_name = str(carrier_freq[i]) + "Hz_" + str(envelope_freq[j]) + "Hz_" + str(duration[k]) + "ms";
#             file_name.append(signal_name)
#             write(signal_name + ".wav", sampling_rate, vibration_signal(i,j,k).astype(np.float16));
#             print("The wav file is successfully saved - filename: " + str(file_name));