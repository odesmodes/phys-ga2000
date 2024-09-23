import numpy as np
from matplotlib import pyplot as plt

N = 100
N_means = 10000 # N is the population, N_means is the mean of each sample of the population

def gaussian(sigma, mu, x):
    a = 1/(sigma*np.sqrt(2*np.pi))
    b = np.exp((-1/2)*((x-mu)/sigma)**2)
    return a * b

y = []
for i in range(0,N_means):
    x = np.random.exponential(scale = 1, size = N_means)
    y.append(np.mean(x))

t = np.linspace(min(y), max(y), 1000)

gauss = [gaussian(np.std(y), np.mean(y), t_i) for t_i in t]

plt.plot(t, gauss)
plt.hist(y, bins = 30, density = True)
plt.savefig('Question_4_part1.png')
plt.show()

# Set initial parameters
N_values = [10, 20, 50, 100, 200, 500, 1000, 1500]  # Different sample sizes
N_means = 10000

def variance(x, mean):
    return np.sum((x - mean) ** 2) / (len(x) - 1)

def skewness(x, mean):
    return np.sum((x - mean) ** 3) / (len(x) * (np.std(x) ** 3))

def kurtosis(x, mean):
    return (1/len(x))*np.sum((x - mean) ** 4) / (len(x) * (np.std(x) ** 4)) 

means = []
variances = []
skewnesses = []
kurtoses = []

for N in N_values:
    y = []
    for i in range(N_means):
        x = np.random.exponential(scale=1, size=N)
        y.append(np.mean(x))
    
    mean_y = np.mean(y)
    means.append(mean_y)
    variances.append(variance(y, mean_y))
    skewnesses.append(skewness(y, mean_y))
    kurtoses.append(kurtosis(y, mean_y))

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(N_values, means, marker='o')
plt.title('Mean vs Sample Size')
plt.xlabel('Sample Size (N)')
plt.ylabel('Mean')

plt.subplot(2, 2, 2)
plt.plot(N_values, variances, marker='o')
plt.title('Variance vs Sample Size')
plt.xlabel('Sample Size (N)')
plt.ylabel('Variance')

plt.subplot(2, 2, 3)
plt.plot(N_values, skewnesses, marker='o')
plt.title('Skewness vs Sample Size')
plt.xlabel('Sample Size (N)')
plt.ylabel('Skewness')

plt.subplot(2, 2, 4)
plt.plot(N_values, kurtoses, marker='o')
plt.title('Kurtosis vs Sample Size')
plt.xlabel('Sample Size (N)')
plt.ylabel('Kurtosis')

plt.tight_layout()
plt.savefig('Question_4_part2.png')
plt.show()
