import numpy as np
import math as m
from scipy import special as sc

def psi(x,n):
    h = sc.eval_hermite(n,x) #Since we are using scipy, might as well use it to evaluate the Hermite polynomial
    return 1/(np.sqrt(2**n*m.factorial(n)*np.sqrt(np.pi)))*h #Note the removal of the exponential term. This is done because the sum of the weights *f is equivalent to the integral of the exponent term * f(x) dx

n = 5   # Wave number
N = 100 # Number of samples

x, w = sc.roots_hermite(N) #Get our weights

s = 0
for k in range(N):
    s+=w[k] * psi(x[k], n)**2*x[k]**2 #Evaluate

print(np.sqrt(s))
