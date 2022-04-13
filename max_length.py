'''Simulates n expriments where we cut a unit stick
and finds the expected value of the largest piece '''

import random as rd

# Cut into two parts:
n = 5000
m = 0
for i in range(1, n+1):
    x = rd.uniform(0,1)
    m = m + max(x, 1-x)
print('Expected length: ', m/n)

# Cut into three parts:
n = 5000
m = 0
for i in range(1, n+1):
    x = rd.uniform(0,1)
    y = rd.uniform(0,1)
    m = m + max(min(x,y), abs(x-y), 1 - max(x,y))
print('Expected length:', m/n)
