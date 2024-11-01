import csv
import matplotlib.pyplot as plt
import jax.numpy as jnp
from jax import grad, hessian, jit
from scipy.optimize import minimize
import numpy as np

def logistic(x,b0,b1):
    return 1/(1+jnp.exp(-(b0+b1*x))) 

#define the negative log likelihood so we can minimize it
def nll(beta):
    prob = logistic(ages, beta[0],beta[1])
    prob_clipped = jnp.clip(prob, 1e-10, 1-1e-10) #we have to make sure that we never take the log of zero or 1 so we clip them to some values which are very close
    return -jnp.sum(recog * jnp.log(prob_clipped) + (1-recog) * jnp.log(1-prob_clipped))

ages = []
recog = []

with open('survey.csv') as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        ages.append(float(row[0]))
        recog.append(float(row[1]))

ages = jnp.array(ages)
ages = (ages - jnp.mean(ages)) / jnp.std(ages) # scale ages from 0 to 1 for machine precision 
recog = jnp.array(recog)

gradient = grad(nll)
hessian_mat = hessian(nll)

beta_init = jnp.array([0.0, 0.0])

result = minimize(lambda b: float(nll(b)), beta_init, jac=lambda b: np.array(gradient(b)))
beta_opt = result.x

hessian_eval = hessian_mat(beta_opt)
cov_mat = np.linalg.inv(hessian_eval)
std_errors = np.sqrt(np.diag(cov_mat))
print("Opt Beta: ", beta_opt)
print("Std Errors: ", std_errors)
print("Cov Mat: ", cov_mat)


age_range = jnp.linspace(min(ages), max(ages),100)
logistic_values = logistic(age_range, *beta_opt)

plt.scatter(ages,recog)
plt.scatter(ages, logistic_values)
plt.savefig('plot.png')

#this doesn't make sense for the data
