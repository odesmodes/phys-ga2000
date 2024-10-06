import matplotlib.pyplot as plt
import numpy as np
import astropy.table

in_table = astropy.table.Table.read('signal.dat', format='ascii.fixed_width')
t=in_table['time']
y=in_table['signal']

dt = (t-t.min()) / (t.max() - t.min()) - 0.5
dt = (t-1.e+9) / 1.e+9 - 0.5

A=np.zeros((len(t),4))
A[:, 0] = 1.
A[:, 1] = dt
A[:, 2] = dt**2
A[:, 3] = dt**3

(u, w, vt) = np.linalg.svd(A, full_matrices=False)
ainv = vt.transpose().dot(np.diag(1./w)).dot(u.transpose())
c=ainv.dot(y)
ym=A.dot(c)

plt.scatter(t,y, label='data')
plt.scatter(t,ym, label='model')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.savefig('PS5-3.png')
plt.close()


residuals = (y-ym).std()
print("Deg 3 Residuals: ", residuals)


nump=40
A=np.zeros((len(t),nump))
for i in np.arange(nump):
    A[:, i] = dt**(i)

(u,w,vt) = np.linalg.svd(A, full_matrices=False)

print(w.max()/w.min())
ainv = vt.transpose().dot(np.diag(1./w)).dot(u.transpose())
c=ainv.dot(y)
ym=A.dot(c)
print("Deg 40 Residuals", (y-ym).std()) #residuals

plt.scatter(t,y, label='data')
plt.scatter(t,ym, label='model')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.savefig('PS5-3_HigherOrder.png')
plt.close()

nperiod = 20

A = np.zeros((len(t), 1 + nperiod * 2 + 3))
A[:, 0] = 1.
nn = np.arange(nperiod, dtype=np.int32) + 1
freqs = np.zeros(1 + nperiod * 2)
for n in nn:
    A[:, n] = np.cos(np.pi * n * (dt + 0.5))
    A[:, n + nperiod] = np.sin(np.pi * n * (dt + 0.5))
    freqs[n] = n
    freqs[n + nperiod] = n
A[:, nperiod * 2 + 1] = dt
A[:, nperiod * 2 + 2] = dt**2
A[:, nperiod * 2 + 3] = dt**3

(u, w, vt) = np.linalg.svd(A, full_matrices=False)

invw = 1. / w
wmax = w.max()
invw[w <= 1.e-7 * wmax] = 0.

ainv = vt.transpose().dot(np.diag(invw)).dot(u.transpose())

c = ainv.dot(y)

ym = A.dot(c)

print("Lomb-Scargle Residuals ", (y-ym).std())

plt.scatter(t, y, label='data')
plt.scatter(t, ym, label='model')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.savefig('PST-3_Lomb-Scargle.png')
plt.close()

plt.scatter(freqs, c[0:len(freqs)]**2, label='power')
plt.xlabel('frequency')
plt.ylabel('coeff')
plt.legend()
plt.savefig('Perodicity.png')
plt.close()
