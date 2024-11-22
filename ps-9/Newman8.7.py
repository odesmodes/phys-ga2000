import numpy as np
import matplotlib.pyplot as plt

m = .5
R = 8/100
v0 = 100
rho = 1.22
C = 0.47
g = 9.81

theta = np.radians(30)

a = 0
b = 20
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)

def f(r, t, m = 0.5):
    x, y, dx, dy = r
    v = np.sqrt(dx**2 + dy**2)
    F_drag = 0.5 * np.pi * R**2 * rho * C * v**2
    ddx = -F_drag/m * dx/v
    ddy = -F_drag/m * dy/v - g
    return np.array([dx,dy,ddx,ddy],float)

def calculate(tpoints, r, h,m=0.5):
    xpoints=[]
    ypoints=[]
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1=h*f(r,t,m)
        k2=h*f(r+0.5*k1,t+0.5*h,m)
        k3=h*f(r+0.5*k2,t+0.5*h,m)
        k4=h*f(r+k3,t+h,m)
        r += (k1+2*k2+2*k3+k4)/6
        if r[1]<0:
            break
    return (xpoints, ypoints)

r = [0.0, 0.0, v0*np.cos(theta), v0*np.sin(theta)]

xpoints,ypoints=calculate(tpoints,r,h,m=1)
plt.plot(xpoints,ypoints)
plt.title("Cannonball Trajectory")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig('8.7 1.png')
plt.close()

res = [calculate(tpoints,r,h,m) for m in np.arange(0.5,5.5,0.5)]
for i,m in zip(res,np.arange(0.5,5.5,0.5)):
    plt.plot(i[0],i[1], label=f"Mass = {m} kg")

plt.title("Cannonball Trajectories")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend(loc='upper left')
plt.savefig('8.7 2.png')
