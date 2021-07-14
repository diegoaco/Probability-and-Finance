
'''Simulates a 1-dimensional random walk'''

import numpy as np 
from random import choices
import matplotlib.pyplot as plt

# Initialise some variables:
n = 500
v = [0]
s = v[0]

# Simulate n coin tosses with outcomes 1 and -1,
# and probabilities p and 1-p
p = 0.5
x = choices([-1,1], [p, 1-p], k = n)

# Compute the cumulative sum s and appends it to the vector v
for i in range(1, n):
    s = s + x[i]
    v.append(s)

# Plots
fig, ax = plt.subplots()
x = np.arange(0, n, 1)
ax.plot(x, v)  
ax.set_xlabel("t")
ax.set_ylabel("S(t)")
plt.show()
