
'''Law of large numbers applied to a coin toss experiment'''

import numpy as np 
from random import choices
import matplotlib.pyplot as plt

# Initialise some variables:
n = 500
v = [0]
s = v[0]
eps = 0.1

# Simulate n coin tosses with outcomes 0 and 1, and their probabilities
p = 0.5
outcomes = [0,1]
prob = [p, 1-p]
x = choices(outcomes, prob, k = n)

# Compute the cumulative sum s and appends it to the vector v
for i in range(1, n):
    s = s + x[i]
    v.append(s)

# Plots the simulated outcomes:
x = np.arange(0, n, 1)
plt.plot(x, v)  
# and the theoretical lines:
plt.plot(x, p*x, c = 'r')
plt.plot(x, (p + eps)*x, c = 'g')
plt.plot(x, (p - eps)*x, c = 'g')
plt.ylabel("Sk")
plt.show()
