# Write a program to make an image of the Mandelbrot set by performing the iteration for all values of c = x + iy on a N x N grid spanning the region where -2 <= x/y <= 2. Make a density plot in which grid points inside the Mandelbrot set are colored black and those outside are colored white.  

import numpy as np
from matplotlib import pyplot as plt

# Define a Mandelbrot function

def mandelbrot(x,y,max_iter):
    c = x + 1j * y # Takes an array of x's and an array of y's and combines them into one complex number array 
    z = np.zeros(c.shape, np.complex64) # Create a z matrix which holds complex numbers and is the same size as c   
    m = np.zeros(c.shape, dtype = int) # Create an m matrix which holds the iteration count (it will be either one or zero in our case so we can see if it is in the mandelbrot set or not)

    for i in range(max_iter):
        mask = np.abs(z) <= 2 # This is an array of booleans which we will use to filter out any numbers that escape the mandelbrot 
        m[mask] = i # Setting our iteration count only where the mask is true
        z[mask] = z[mask]**2 + c[mask] # Calculates the value of z where the mask is true 
        m = (m == max_iter - 1).astype(int) # Takes the m iteration counter and removes everything that isn't the maximum number of iterations

    return(m)

# Setup grid

arr = np.linspace(-2,2,5000)
x,y = np.meshgrid(arr,arr)
max_iter = 200

m = mandelbrot(x,y,max_iter) # Calculating the mandelbrot

plt.imshow(m,cmap = 'gray_r') # Image show plots image data, color map is grey
plt.title('Mandelbrot Set Density Plot')
plt.savefig('Mandelbrot_Plot', format ='png') 
