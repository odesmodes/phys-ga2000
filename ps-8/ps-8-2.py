import matplotlib.pyplot as plt
import numpy as np
import scipy

#following the example 8.5
sigma = 10
_r = 28
_b = (8/3)
def f(t,r):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y - x)
    fy = _r*x - y - x*z
    fz = x*y - _b*z
    return [fx,fy,fz]

a=0
b=50.0
t_span = (a,b)
t_eval = np.linspace(a, b, 10000)
r0 = [0,1,0]

solution = scipy.integrate.solve_ivp(f, t_span, r0, t_eval=t_eval)

xpoints = solution.y[0]
ypoints = solution.y[1]
zpoints = solution.y[2]
tpoints = solution.t

plt.plot(tpoints,ypoints)
plt.savefig('PartA.png')
plt.show()
plt.close()

plt.plot(xpoints,zpoints)
plt.savefig('StrangeAttr.png')
plt.show()
