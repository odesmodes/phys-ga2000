# Starting with a sample consisting of 10000 atoms of Bi, simulate the decay of the atoms as in Example 10.1 by dividing time into slices of length 1s and on each step doing the following:

import numpy as np
from matplotlib import pyplot as plt
from random import random

# Constants
NBi_213 = 10000
NTl = 0
NPb = 0
NBi_209 = 0
tau_Bi213 = 46*60 # Half life of Bi in seconds
tau_Tl = 2.2*60
tau_Pb = 3.3*60
time_step = 1 
pBi_213 = 1 - 2**(-time_step/tau_Bi213)
pTl = 1 - 2**(-time_step/tau_Tl)
pPb = 1 - 2**(-time_step/tau_Pb)
total_time = 20000

# Lists of plot points
tpoints = np.arange(0, total_time, time_step)
Bi213points = []
Tlpoints = []
Pbpoints = []
Bi209points = []

# Part a
for t in tpoints:
    Pbpoints.append(NPb)
    Bi209points.append(NBi_209)

    # Calculating number of atoms that decay
    decay = 0
    for i in range(NPb):
        if random()<pPb:
            decay += 1
    NPb -= decay
    NBi_209 += decay

# Part b
    Tlpoints.append(NTl)

    # Calculating number of atoms that decay
    decay = 0
    for i in range(NTl):
        if random()<pTl:
            decay += 1
    NTl -= decay
    NPb += decay

# Part c
    Bi213points.append(NBi_213)
    
    # Calculating number of atoms that decay
    decay = 0
    for i in range(NBi_213):
        if random()<pBi_213:
            decay += 1
            if random()<0.9791: # Accounting for the two route possibility
                NBi_213 -= decay
                NPb += decay
            else:
                NBi_213 -= decay
                NTl += decay


print(NBi_213, NTl, NPb, NBi_209)
print(tpoints)

# Plotting the graph
plt.plot(tpoints,Bi213points)
plt.plot(tpoints,Pbpoints)
plt.plot(tpoints,Tlpoints)
plt.plot(tpoints,Bi209points)
plt.xlabel("Time")
plt.ylabel("Number of Atoms")
plt.legend(['Bi_213', 'Pb', 'Tl', 'Bi_209'])
plt.title('Decay of Bi_213 Isotope')
#plt.show()
plt.savefig('DecayGraph.png')

