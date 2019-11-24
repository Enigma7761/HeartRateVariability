
from ctypes import *
from matplotlib import pyplot as plt
import numpy as np

def ecg_from_file(ecg, filename):
    f = open(filename, 'r')
    for x in f:
        ecg.append(float(x[x.index(',') + 1:x.index('\n')]))
    f.close()

def signal_from_file(signal, filename):
    f = open(filename,'r')
    for x in f:
        signal.append(float(x))
    f.close()
    return signal

def plot(ecg, signal):
    x = range(ecg.shape[0])
    plt.plot(x, ecg)
    plt.plot(x, signal)
    plt.show()

ecg = []
signal = []
signal2 = []
ecg_from_file(ecg,"../ECG_Data/T21.ascii")
signal_from_file(signal, "../Signal/SignalCorrected.txt")
'''
signal_from_file(signal2,"Signal.txt")
signal_from_file(ecg2,"ECG.txt")
signal = signal_from_file(signal,"Sample1Corrected.txt")
ecg = ecg_from_file(ecg,"Sample 2.ascii")
signal = signal_from_file(signal, "Sample2Corrected.txt")
ecg = ecg_from_file(ecg,"Sample 3.ascii")
signal = signal_from_file(signal,"Sample3Corrected.txt")
ecg = ecg_from_file(ecg,"Sample 4.ascii")
signal = signal_from_file(signal, "Sample4Corrected.txt")
ecg = np.asarray(ecg)
ecg = np.append(ecg,-ecg)
signal = np.asarray(signal)
signal = np.append(signal,signal)
ecg = ecg.reshape(ecg.shape[0],1)
signal = signal.reshape(signal.shape[0],1) 
#plt.plot(range(len(signal2)),signal2)
#plt.plot(range(len(ecg2)),ecg2)
'''
plt.plot(range(len(signal)),signal)
plt.plot(range(len(ecg)),ecg)
plt.show()