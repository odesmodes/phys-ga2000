import numpy as np
import matplotlib.pyplot as plt


#7.3
#the code is pretty straight forward
samplerate = 44100
waveform = []
with open('piano.txt','r') as file:
    for line in file:
        waveform.append(int(line.rstrip()))
    file.close()

plt.plot(waveform)
plt.title('Piano Wave')
plt.xlabel('Sample Number')
plt.ylabel('Magnitude')
plt.savefig('piano.png')
plt.show()
plt.close()

coeffs = np.fft.fft(waveform)
freqs = np.fft.fftfreq(len(coeffs),d=1/samplerate)
plt.plot(freqs[:10000], np.abs(coeffs[:10000]))
plt.title('Piano FFT')
plt.xlabel('Freq (Hz)')
plt.ylabel('Magnitude (dB)')
plt.savefig('piano FFT.png')
plt.show()

waveform = []
with open('trumpet.txt','r') as file:
    for line in file:
        waveform.append(int(line.rstrip()))
    file.close()

plt.plot(waveform)
plt.xlabel('Sample Number')
plt.ylabel('Magnitude')
plt.title('Trumpet Wave')
plt.savefig('trumpet.png')
plt.show()
plt.close()

coeffs = np.fft.fft(waveform)
freqs = np.fft.fftfreq(len(coeffs),d=1/samplerate)
plt.plot(freqs[:10000], np.abs(coeffs[:10000]))
plt.xlabel('Freq (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Trumpet FFT')
plt.savefig('TrumpetFFT.png')
plt.show()

#a.
#The coefficients tell us the fundamental and the other harmonics that make up the timbre of an instrument.
#We can see with the piano most of the sound comes from the fundamental, while the trumpet actually has a greater contribution from the first harmonic. 

#b. They are both playing C5, one octave above middle C, although the trumpet seems a little flat 
