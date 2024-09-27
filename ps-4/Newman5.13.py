import numpy as np
import math as m
from matplotlib import pyplot as plt

# part a 
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

n_range = np.arange(0,4,1);
x_range = np.linspace(-4,4,1000);

figure, axis = plt.subplots(2,1)

for i in n_range:
    n_res = []
    for j in x_range:
        n_res.append(psi(j,i))
    axis[0].plot(x_range,n_res)
    axis[0].set_title("n range 0 to 4")

# Part b
n = 30
x_range2 = np.linspace(-10,10,1000)

n_res2 = [psi(i,n) for i in x_range2]

axis[1].plot(x_range2,n_res2)

plt.xlabel('x [m]')
axis[0].set_ylabel('Psi_n(x)')
axis[1].set_ylabel('Psi_30(x)')
axis[0].legend(n_range, loc=1)
plt.savefig('Q3partab.png')
plt.show()
