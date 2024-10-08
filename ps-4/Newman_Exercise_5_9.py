# Heat capacity of a solid
import numpy as np
from matplotlib import pyplot as plt

# Copied gaussian quadrature function from appendix E 

def gaussxw(N): 
    a = np.linspace(3,4*N,N)/(4*N+2)
    x = np.cos(np.pi*a+1/(8*N*N*np.tan(a)))
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = np.ones(N,float)
        p1 = np.copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gausswab(N,a,b): # Gaussian weights a to b
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

# Writing out the function to integrate that they gave in the problem

def f(x):
    return (x**4*np.e**x)/(np.e**x-1)**2

# Finally. Writing the python function cv(T)
# Part a
def cv(T,N):

    # Parameters that they gave in the problem
    rho = 6.022e28 #m^-3
    debye = 428 # K
    V = 1e-6 # cm -> m
    k = 1.38e-23 # J*K^-1
   
    linear = 9 * V * rho * k * (T/debye)**3 # This is the linear part of Cv
    x,w = gausswab(N,0,debye/T) # Getting the weights and x values (to evaluate the function at point x and multiply by the weights
    s=0
    for k in range(N): # summation/integral
        s+=w[k]*f(x[k]) # w is an array of our weights * the integrand
    return linear*s

# plotting
# part b

temp_range = np.linspace(5,500,1000)
cv_res = [cv(i,50) for i in temp_range]

#plt.plot(temp_range, cv_res)
#plt.xlabel('Temperature Range [K]')
#plt.ylabel('Cv(T) [J/K]')
#plt.savefig('Cv(T).png')
#plt.show()

# part c: Test the convergence by evaluating the choices N = 10,20,30,40,50,60,70
# using a for loop to do this easier

nrange = np.arange(10,80,10)

for i in nrange:
    cv_res_2 = []
    for j in temp_range:
        cv_res_2.append(cv(j,i))
    plt.plot(temp_range, cv_res_2)

plt.legend(nrange)

plt.xlabel('Temperature Range [K]')
plt.ylabel('Cv(T) [J/K]')
plt.savefig('convergence_test.png')
#plt.show()


        
