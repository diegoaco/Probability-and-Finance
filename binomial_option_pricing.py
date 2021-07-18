'''IMPLEMENTS A RISK-HEDGING ALGORITHM UNDER THE MULTISTEP 
BINOMIAL MODEL TO PRICE AN OPTION FOR A RANGE OF EXPIRY TIMES'''

import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 10   # Max expiry time
s0, K, r = 4, 5, 1/4
u, d = 2, 1/2
D = 1/(1+r) # discrete discount factor

# Risk-free probabilities
p = ((1/D)-d)/(u-d)
q = 1 - p

# Payoff function (put option)
def payoff(S, K):
    return np.array([max(i - K, 0) for i in S])

x = np.arange(1, m+1, 1)
y = []

for n in x:
    # Create the possible values of the stock
    S = np.array([s0*(u**i)*(d**(n-i)) for i in range(n,-1,-1)])
    # Creates a zero matrix
    c = np.zeros([n+1,n+1])
    c[-1] = payoff(S,K)
    # Risk-hedging algorithm:
    for i in range(n-1, -1, -1):
        for j in range(0, i+1):
            c[i][j] = D*(p*c[i+1][j] + q*c[i+1][j+1])
    y.append(c[0][0])  # Store the option prices for each time

# Plot the results and the bounding curves:
plt.plot(x,y)
plt.plot(x, np.array([s0 - K*(D**i) for i in x]))
plt.hlines(s0, 0, m, color = 'r')

# Presents the data as a time series 
A = np.column_stack((x, y))
print(A)
