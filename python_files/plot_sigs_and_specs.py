import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pyaudio
import pandas as pd

# short function to plot wav audio file - raw signal and spectrogram
def plot_audio_signal(filename,subplot_title,axa,axb):
    # load in audio file
    spf = wave.open(filename,'r')

    # extract audio from wav file
    sig = spf.readframes(-1)
    sig = np.fromstring(sig, 'Int16')
    fs = spf.getframerate()
    Time=np.linspace(0, len(sig)/fs, num=len(sig))

    # set up figure and plot
    axa.set_title(subplot_title)
    axa.plot(Time,sig,color = 'r')
    axa.set_yticks([],[])
    axa.axis('off')  
   
    # plot spectrogram
    axb.specgram(sig, NFFT=128, noverlap=0)
    axb.set_yticks([],[])
    axb.axis('off') 
    
def plot_all():
    # plot 3 signals for comparison
    # create subplot figure
    fig = plt.figure(figsize = (10,4))
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)

    # feed in each audio signal 
    plot_audio_signal('audio_files/dog1.wav','dog',ax1,ax4)

    # feed in each audio signal 
    plot_audio_signal('audio_files/dog2.wav','dog',ax2,ax5)

    # feed in each audio signal 
    plot_audio_signal('audio_files/cat.wav','cat',ax3,ax6)