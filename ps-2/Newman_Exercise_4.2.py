# Part a: Write a program that takes as input the three numbers a, b, and c and prints out the two solutions using the standard quadratic equation formula and use your program to compute the solutions of 0.001x**2 + 1000x + 0.001 = 0. 

import numpy as np

a = 0.001
b = 1000
c = 0.001

def quadratic(a,b,c):
    return( (-b + np.sqrt(b**2 - 4*a*c))/(2*a),(-b - np.sqrt(b**2 - 4*a*c))/(2*a) )

print(quadratic(a,b,c))

# Part b: Same but use different quadratic equation formula

def altquadratic(a,b,c):
    return( (2*c)/(-b - np.sqrt(b**2 - 4*a*c)),(2*c)/(-b + np.sqrt(b**2 - 4*a*c)) )

print(altquadratic(a,b,c))

# Part c: Make them equivalent
# Use one method for minus and the other method for plus so that when we divide we get a small number so that we don't ruin our precision

def accquadratic(a,b,c):
   
    if b >= 0:
        root1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (2*c)/(-b + np.sqrt(b**2 - 4*a*c))

    else:
        root2 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
        root1 = (2*c)/(-b + np.sqrt(b**2 - 4*a*c))

    return(root1, root2)

print(accquadratic(a,b,c))
