import matplotlib.pyplot as plt
import numpy as np
d=[]
with open("dow.txt","r") as f:
    for line in f.readlines():
        n=float(line)
        d.append(n)

plt.plot(d)
plt.xlabel('year')
plt.ylabel('points')

coeffs = np.fft.rfft(d)
tcoeffs=coeffs[:int(len(coeffs)*.1)]

icoeffs = np.fft.irfft(tcoeffs,len(d))
plt.plot(icoeffs)
plt.title('10% Coeffs')
plt.savefig('10_Coeffs.png')
plt.close()

plt.plot(d)
plt.xlabel('year')
plt.ylabel('points')

vtcoeffs=coeffs[:int(len(coeffs)*0.02)]
icoeffs=np.fft.irfft(vtcoeffs,len(d))

plt.plot(icoeffs)
plt.title('2% Coeffs')
plt.savefig('2_Coeffs.png')
plt.close()
