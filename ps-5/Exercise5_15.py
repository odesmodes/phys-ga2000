# Create a user defined function f(x) that returns the value 1 + 1/2tanh2x
from jax import grad
import jax.numpy as jnp
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return 1 + (1/2) * jnp.tanh(2*x)

# Use central difference to calculate the derivative of the function in the range -2 to 2

def central_deriv(x):
    return (f(x + h/2) - f(x - h/2))/h

rng = np.linspace(-2, 2, 150) 
h = 0.0001 # Picked it to be a small number

numeric = [central_deriv(x) for x in rng]

# Calculate an analytic formula for the derivative

analytic = [((1/jnp.cosh(2*x)))**2 for x in rng]

# Use jax to calculate same derivative

jax = grad(f)
autodiff = [jax(x) for x in rng]

# Plot numeric and analytic and jax on same plot

plt.plot(rng, analytic, color = 'orange',label = 'Analytic')
plt.scatter(rng, numeric, marker = 'o', label = 'Numeric')
plt.scatter(rng, autodiff, marker = 'x', label = 'Using Jax', color = 'yellow')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.savefig('Q1.png')





