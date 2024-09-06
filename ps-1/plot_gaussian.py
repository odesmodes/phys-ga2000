# PS-1 Q2

# Importing libraries
# numpy: math package
# matplotlib: some math plotting stuff- only using pyplot because we don't really need anything else
import numpy as np 
from matplotlib import pyplot as plt

# Define Gaussian function
def gaussian(x,sigma,mu):
    return (1/(np.sqrt(2 * np.pi * sigma))) * np.e**-((x-mu)**2/(2 * sigma**2))
#return not print so that we can do stuff with it later ie plot

# Setup plotting function (to plot we need x and y)
# First setup range (x) of plot using np.linspace to set number of plot points in between extremes
x = np.linspace(-10,10,100)
# Then we can find the results of our gaussian (y) for each x from the array above and store them as a list
# To make list [] then use a for loop to iterate through array 
y = [gaussian(x_i,3,0) for x_i in x] 

# Now we can plot using pyplot
plt.plot(x,y)

# Labeling the axes
plt.xlabel("Gaussian Range")
plt.ylabel("Gaussian")
plt.title("Normalized Gaussian Function")

# Save the plot:
plt.savefig("gaussian.png")
