''' Simulates n expriments where we cut a unit stick
and finds the expected value of the largest piece '''

import random

n = 1000
m = 0
for i in range(1,n+1):
    x = random.uniform(0,1)
    m = m + max(x, 1-x)
print('Expected length:', m/n)
