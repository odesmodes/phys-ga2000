import numpy as np
from gaussxw import gaussxw, gaussxwab 
from matplotlib import pyplot as plt

mass = 1 
N = 20
linear = np.sqrt(8 * mass)
amp_range = np.linspace(0.1,2,100) # Not starting at zero to avoid division by zero error

def potential_function(x,a):
    return 1/np.sqrt(a**4-x**4)

def T(N,a):
    x,w = gaussxwab(N,0,a)
    s = 0 
    for k in range(N):
        s += w[k] * potential_function(x[k], a)
    return s*linear

res_range = [T(N,a) for a in amp_range]

plt.plot(amp_range, res_range)
plt.xlabel("Amplitude [m]")
plt.ylabel("Period [s]")
plt.savefig('Q2.png')
