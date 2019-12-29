from matplotlib import pyplot as plt
import numpy as np
import os
from Methods import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Dense, Dropout, Flatten, MaxPooling1D, Activation
import tensorflow as tf

interval_length = 400
step = 100

Model = Sequential()
Model.add(Conv1D(input_shape = (interval_length,1), filters = 20, kernel_size = 4,strides = 2, activation = 'relu'))
Model.add(MaxPooling1D())
Model.add(Conv1D(50, kernel_size = 8, strides = 2, activation = 'relu'))
Model.add(MaxPooling1D())
Model.add(Flatten())
Model.add(Dense(600))
Model.add(Activation('relu'))
Model.add(Dropout(0.2))
Model.add(Dense(interval_length))
Model.add(Activation('softmax'))
Model.load_weights("Model.h5")

ecg = []
ecg_from_file(ecg, os.path.join('..','ECG_Data','T21.ascii'))
signal = np.zeros((len(ecg)))

with tf.device("/device:CPU:0"):
    for i in range(0,len(ecg) - interval_length,step):
        if i % 10000 == 0:
            print(i)
        temp = np.asarray(ecg[i:i+interval_length])*100
        temp = Model.predict(temp.reshape(1,interval_length, 1))
        if np.var(temp) > 0.01:
            continue
        else:
            temp -= np.average(temp)
            signal[i:i + interval_length] += temp.reshape(400,)

signal /= (interval_length/step)

f = open(os.path.join('..','Signal','SignalPy.txt'),'w')
for i in signal:
    f.write(str(i) + '\n')
f.close()

plt.plot(range(len(ecg)), ecg)
plt.plot(range(len(signal)), signal)
plt.axis([0,6000,-0.5,1])
plt.show()