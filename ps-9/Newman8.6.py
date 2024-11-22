import numpy as np
import matplotlib.pyplot as plt


#for A
def f(r,t):
    x = r[0]
    dx = r[1]
    fx = dx
    fdx = -omega**2*x
    return np.array([fx,fdx],float)

#for C
def f2(r,t):
    x = r[0]
    dx = r[1]
    fx = dx
    fdx = -omega**2*x**3
    return np.array([fx,fdx],float)

#for E
def f3(r,t):
    x = r[0]
    dx = r[1]
    fx = dx
    fdx = -omega**2*x + mu*(1-x**2)*dx
    return np.array([fx,fdx],float)

#for A,B
def calculate(tpoints, r, h):
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return (xpoints, ypoints)

#for C
def calculate2(tpoints, r, h):
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f2(r,t)
        k2 = h*f2(r+0.5*k1,t+0.5*h)
        k3 = h*f2(r+0.5*k2,t+0.5*h)
        k4 = h*f2(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return (xpoints, ypoints)

#E
def calculate3(tpoints, r, h):
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f3(r,t)
        k2 = h*f3(r+0.5*k1,t+0.5*h)
        k3 = h*f3(r+0.5*k2,t+0.5*h)
        k4 = h*f3(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return (xpoints, ypoints)

#part A

omega = 1

a = 0
b = 50
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
r = np.array([1.0,0.0],float)
xpoints, ypoints = calculate(tpoints, r, h)

plt.title("Second order: x = 1")
plt.xlabel("time (t)")
plt.ylabel("Amplitude (y)")
plt.plot(tpoints,xpoints)
plt.savefig('plot1.png')
plt.close()

#part B

r = np.array([2.0,0.0],float)
xpoints, ypoints = calculate(tpoints, r, h)

plt.title("Second order: x = 2")
plt.xlabel("time (t)")
plt.ylabel("Amplitude (y)")
plt.plot(tpoints,xpoints)
plt.savefig('plot2.png')
plt.close()


r = np.array([1.0,0.0],float)
xpoints, ypoints = calculate2(tpoints, r, h)

plt.title("Second order, x^3: x = 1")
plt.xlabel("time (t)")
plt.ylabel("Amplitude (y)")
plt.plot(tpoints,xpoints)
plt.savefig('plot3.png')
plt.close()

r = np.array([2.0,0.0],float)
xpoints, ypoints = calculate2(tpoints, r, h)

plt.title("Second order, x^3: x = 2")
plt.xlabel("time (t)")
plt.ylabel("Amplitude (y)")
plt.plot(tpoints,xpoints)
plt.savefig('plot4.png')
plt.close()


#part D

plt.title("Second order, x^3: Phase Space")
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.plot(xpoints,ypoints)
plt.savefig('plot5.png')
plt.close()

#part E

mu = 1

a = 0
b = 20
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
for mu in [1,2,4]:
    r = np.array([1.0,0.0],float)
    xpoints, ypoints = calculate3(tpoints, r, h)
    plt.title(f"Van der Pol Phase Space: mu = 1,2,4")
    plt.xlabel("x")
    plt.ylabel("dx/dt")
    plt.plot(xpoints,ypoints, label= f"mu = {mu}")
plt.legend()
plt.savefig('plot6.png')
plt.close()

