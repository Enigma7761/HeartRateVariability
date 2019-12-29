from Methods import *
import os.path
from matplotlib import pyplot as plt


ecg = []
averaged = []
test = []
inverted = []
signal = []
#fig, axs = plt.subplots(3, sharex = True)
ecg_from_file(ecg, os.path.join('..','ECG_Data','T21.ascii'))
signal_from_file(averaged, os.path.join('..','Signal','Averaged.txt'))
signal_from_file(test, os.path.join('..','Signal','Test.txt'))
signal_from_file(inverted, os.path.join('..','Signal','Inverted.txt'))
signal_from_file(signal, os.path.join('..','Signal','SignalPy.txt'))

'''
axs[0].plot(range(len(ecg)), ecg)
axs[1].plot(range(len(test)), test)
axs[2].plot(range(len(inverted)), inverted)
axs[0].axis([0,6000,-1,1])
axs[1].axis([0,6000,800,1400])
axs[2].axis([0,6000,-1.2,1.2])
'''

plt.plot(range(len(ecg)),ecg)
plt.plot(range(len(signal)),signal)
plt.axis([0,6000,-0.5,1])
plt.show()