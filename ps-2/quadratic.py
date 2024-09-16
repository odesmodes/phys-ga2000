# Solver Module
import numpy as np

def quadratic(a,b,c):
   
    if b >= 0:
        root1 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (2*c)/(-b - np.sqrt(b**2 - 4*a*c))

    else:
        root2 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
        root1 = (2*c)/(-b + np.sqrt(b**2 - 4*a*c))

    return root2, root1