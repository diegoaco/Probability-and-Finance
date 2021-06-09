''' Simulates two people arriving at random times
and waiting for at most a time a. Calculates the
probability they meet and, if they do, the expected
time they have to wait'''

import random

n = 10000 
l, a = 60, 10
c, e = 0, 0
for i in range(1,n+1):
    x = [random.uniform(0,l) for _ in range(2)]
    z = abs(x[0] - x[1])
    if z <= a:
        c = c + 1
        e = e + z
    else: continue 
print('Probability they meet:', c/n)
print('Expected time:', e/n)
