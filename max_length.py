''' Simulates n expriments where we cut a unit stick
and finds the expected value of the largest piece '''

import random

n = 1000
c, m = 0, 0
for i in range(1,n+1):
    x = [random.uniform(0,1)]
    a = x[0]
    b = 1 - x[0]
    m = m + max(a,b)
print('Expected length:', m/n)
