''' Plots earthquakes data folloing a Poisson distribution
and compares them to the analytical model'''

import numpy as np
import matplotlib.pyplot as plt
import math

# Mexico City data
x = np.arange(0, 7, 1)
n = [61, 40, 15, 2, 2, 0, 0]

# California data
'''x = np.arange(0,14,1)
n = [18, 29, 22, 23, 10, 6, 3, 3, 1, 1, 2, 1, 1, 0]'''

# Compute the proportions (probabilities) and lambda
y = np.array([i/sum(n) for i in n])
lam = np.dot(x,n)/sum(n)

# Theoretical model
def fun(t, x):
    return math.exp(-t*lam)*((t*lam)**x)/math.gamma(x+1)

x1 = np.arange(0, len(x)-1, 0.1)
y1 = np.array([fun(1, i) for i in x1])

# Plot
fig, ax = plt.subplots()
ax.plot(x, y, 'o', label = 'Data')
ax.plot(x1, y1, label = 'Poisson distribution')
ax.set_ylabel("P(X = k)")
ax.set_xlabel("Earthquakes per year (k)")
leg = ax.legend()
plt.show()
