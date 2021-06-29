
'''Central Limit Theorem applied to a sequence of dice rolls'''

import math
import numpy as np 
from random import choices
import matplotlib.pyplot as plt

# Toss n times and carry out n of these experiments
# Porbability of success is p
n, p = 12000, 1/6
s, y = [], []
q = 1 - p

# Simulate n coin tosses with outcomes 0 and 1, and their probabilities
for j in range(1, n):
    # Compute the cumulative sum s and appends it to the vector s
    x = choices([1,0], [p,q], k = n)
    s.append(sum(x))
    
# Define the interval of interest [a,b] and find the
# probability of the sum being equal to some k in [a,b]  
a, b = int(n/6 - 200),  int(n/6 + 200)
x = np.arange(a, b+1, 1)
for i in x:
    prob = s.count(i)/n
    y.append(prob)

# Theoretical distribution
def normal(x):
    return (1/math.sqrt(2*math.pi*n*p*q))*math.exp(-((x-n*p)**2)/(2*n*p*q))
  
# Plot
y1 = np.array([normal(i) for i in x])

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot(x, y1)
ax.set_xlabel("k")
ax.set_ylabel("P(Sn = k)")
