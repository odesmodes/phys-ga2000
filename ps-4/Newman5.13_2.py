import numpy as np
import math as m
from gaussxw import gaussxw, gaussxwab

# part c
def H(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    H0, H1 = 1, 2 * x
    for i in range(2, n+1):
        Hn = 2 * x * H1 - 2 * (i-1) * H0
        H0, H1 = H1, Hn
    return H1

def psi(x,n):
    return 1/(np.sqrt(2**n*m.factorial(n)*np.sqrt(np.pi)))*np.e**(-x**2/2)*H(x,n)

def cov(z,n):
    linear = ((z/(1-z**2))**2)*(1+z**2)/((1-z**2)**2) #x**2 * the part that pops out
    f = psi((z/(1-z**2)),n) 
    return linear*np.abs(f)**2

#def cov(z,n): # this one doesn't work for some reason
#    linear = np.tan(z)**2
#   f = psi(np.tan(z),n)/np.cos(z)**2
#    return linear * np.abs(f)**2

N = 100
n = 5
a = -1
b = 1

x,w = gaussxwab(N,a,b)

s=0
for k in range(N):
    s+=w[k]*cov(x[k],n)
print(np.sqrt(s))
    
# part d
