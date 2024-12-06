from banded import banded
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 1000
m = 9.109e-31
#L = 10e-8
L = 1e-8
a = L/N
h = 10e-18
#hbar = 1.05457e-34
hbar = 1.05457e-36

x = np.linspace(0,L,N+1)

x0 = L/2
sigma = 1e-10
k = 5e10

psi0 = np.exp(-(x-x0)**2 / (2*sigma**2)) * np.exp(1j * k * x)
psi0[0], psi0[-1] = 0,0

psi = psi0.copy()

a1 = 1 + h*(1j*hbar)/(2*m*a**2)
a2 = -h*(1j*hbar)/(4*m*a**2)
b1 = 1 - h*(1j*hbar)/(2*m*a**2)
b2 = h*(1j*hbar)/(4*m*a**2)

#construct matrices
A = np.zeros((3, N-1), dtype=complex)
B = np.zeros((3, N-1), dtype=complex)

#Set the diagonals to a1 and the others to a2

A[1,:] = a1
A[0,1:] = a2
A[2,:-1] = a2

B[1,:] = b1
B[0,1:] = b2
B[2,:-1] = b2

for _ in range(100):
    v = (b1*psi0[1:N] + b2*(psi0[2:N+1] + psi0[0:N-1]))
    psi0[1:N] = banded(A,v,1,1)
    psi0[0],psi0[-1] = 0, 0

plt.plot(psi0)
plt.xlabel('Position (m)')
plt.ylabel('Psi')
plt.title('Wavefunc after 100 steps')
plt.savefig('100 steps.png')
plt.close()

def evo_func():
    v = (b1*psi[1:N] + b2*(psi[2:N+1] + psi[0:N-1]))
    psi[0],psi[-1] = 0, 0
    psi[1:N] = banded(A,v,1,1)

fig, ax = plt.subplots()
line, = ax.plot(x, np.real(psi0))

def update(frame):
    evo_func()
    line.set_ydata(np.real(psi))
    return line, 
ani = FuncAnimation(fig, update, frames=200000,interval=50,blit=True)
ani.save("wavefunc.mp4",fps=30,writer="ffmpeg")
