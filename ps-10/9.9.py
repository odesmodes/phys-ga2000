import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dcst import dst, idst

L = 1e-8
M = 9.109e-31
N = 1000
h = 20e-18
hbar = 1.05457e-36

x = np.linspace(0, L, N + 1)
x0 = L / 2
sigma = 1e-10
k = 5e10

psi0 = np.exp(-(x-x0)**2 / (2*sigma**2)) * np.exp(1j * k * x)
psi0[0],psi0[-1] = 0,0

psi = psi0.copy()

b0r = dst(np.real(psi0))
b0i = dst(np.imag(psi0))
b0 = b0r + 1j * b0i

t = 10e-16
b_k = b0*np.exp(1j * (np.pi **2 * hbar *(np.arange(1, N+2)**2)) * t / (2* M * L**2))

psi_kr = idst(np.real(b_k))
psi_ki = idst(np.imag(b_k))
psi_k = psi_kr + 1j * psi_ki
plt.plot(psi_k)
plt.xlabel('Position (m)')
plt.ylabel('Psi')
plt.title('Wavefunc at t = 10e-16s')
plt.savefig('wavefunc_spec.png')
plt.close()

fig, ax = plt.subplots()
line, = ax.plot(x, np.real(psi0))
ax.set_xlim(0,L)

def update(frame):
    t = frame * h*10
    b_k_ = b0*np.exp((-1j * (np.pi **2 * hbar *(np.arange(1, N+2)**2)) * t) / (2 * M * L**2))
    psir = idst(np.real(b_k_))
    psii = idst(np.imag(b_k_))
    psi = psir + 1j * psii
    psi[0],psi[-1] = 0,0
    line.set_ydata(np.real(psi))
    return line,
ani = FuncAnimation(fig, update, frames = 200000, interval = 50, blit =True)
ani.save("wavefunc_spectral.mp4",fps=30,writer="ffmpeg")
