import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import pandas as pd

# load in 3 simple prototype signals
data1 = np.asarray(pd.read_csv('datasets/simple_signal_1.csv'))
data2 = np.asarray(pd.read_csv('datasets/simple_signal_2.csv'))
data3 = np.asarray(pd.read_csv('datasets/simple_signal_3.csv'))

# plot signals
fig = plt.figure(figsize = (10,4))
ax = fig.add_subplot(231)
ax.plot(data1[:,0],data1[:,1],color = 'r')
ax.set_yticks([],[])
ax.axis('off')  

ax = fig.add_subplot(232)
ax.plot(data2[:,0],data2[:,1],color = 'r')
ax.set_yticks([],[])
ax.axis('off')  

ax = fig.add_subplot(233)
ax.plot(data3[:,0],data3[:,1],color = 'r')
ax.set_yticks([],[])
ax.axis('off')  

# plot dfts
ax = fig.add_subplot(234)
DFT = np.fft.rfft(data1[:,1])
ax.stem(np.arange(10),np.abs(DFT[0:10]),markerfmt=" ")
ax.set_yticks([],[])
ax.axis('off') 
ax.set_xlim([-0.1,10.1])
ax.set_ylim([-1,max(np.abs(DFT))+0.5])

ax = fig.add_subplot(235)
DFT = np.fft.rfft(data2[:,1])
ax.stem(np.arange(10),np.abs(DFT[0:10]),markerfmt=" ")
ax.set_yticks([],[])
ax.axis('off') 
ax.set_xlim([-0.1,10.1])
ax.set_ylim([-1,max(np.abs(DFT))+0.5])

ax = fig.add_subplot(236)
DFT = np.fft.rfft(data3[:,1])
ax.stem(np.arange(10),np.abs(DFT[0:10]),markerfmt=" ")
ax.set_yticks([],[])
ax.axis('off') 
ax.set_xlim([-0.1,10.1])
ax.set_ylim([-1,max(np.abs(DFT))+0.5])