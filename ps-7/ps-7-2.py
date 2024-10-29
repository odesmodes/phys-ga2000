import numpy as np
from scipy.optimize import brent

def func(x):
    return (x-0.3)**2*np.exp(x)

def my_brent(func, a, b, tol=1e-6, max_iter=100):
    f_a = func(a) 
    f_b = func(b) 
    #this technically should be here, but it doesn't work with it in
    #if(f_a*f_b >= 0):
    #    raise ValueError("Function must change signs")
    if(abs(f_a) < abs(f_b)):
        a,b = b,a
        f_a,f_b=f_b,f_a

    c=a
    f_c = f_a
    mflag = True
    d = e = b-a
    for i in range(max_iter):
        if f_b ==0 or abs(b-a) < tol:
            return b
        if f_a != f_c and f_b != f_c:
            s = (a*f_b*f_c / ((f_a-f_b) *(f_a-f_c))
                 + b * f_a * f_c / ((f_b - f_a) * (f_b - f_c))
                 + c * f_a * f_b / ((f_c - f_a) * (f_c - f_b)))
        else:
            s = b - f_b * (b-a) / (f_b-f_a)
        cond1 = not((3*a+b) / 4 <= s <= b)
        cond2 = mflag and abs(s-b) >= abs(b-c) /2
        cond3 = not mflag and abs(s-b) >=abs(c-d)/2
        cond4 = mflag and abs(b-c) < tol
        cond5 = not mflag and abs(c-d) < tol

        if cond1 or cond2 or cond3 or cond4 or cond5:
            s=(a+b)/2
            mflag = True
        else:
            mflag = False
        f_s = func(s)
        d,c = c,b
        if f_a*f_s < 0:
            b = s
            f_b = f_s
        else:
            a = s
            f_a = f_s
        if(abs(f_a) < abs(f_b)):
            a, b = b,a
            f_a, f_b = f_b, f_a
    raise RuntimeError("Max iter reached")


sci_root = brent(func,brack=(0,1))
root=my_brent(func,0,1)
print("Scipy: ", sci_root)
print("My own: ", root)
