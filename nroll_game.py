from random import choices

m = 1000   # Number of games
y = [0]    # List storing the expected values

def exp(n):
    if n == 0:
        return 0
    else:
        a = exp(n-1)
        sum = 0
        for i in range(1, m + 1):   # Loop playing m games
            for j in range(1,n+1):  # Loop playing a n-roll game
                outcomes = [1,2,3,4,5,6]
                prob = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
                x = choices(outcomes, prob, k = 1)
                # Implementation of the strategy
                if x[0] > y[-j]:
                    sum = sum + x[0]
                    break
                elif j == n:
                    sum = sum + x[0]
        y.append(sum/m)   # Add the expected value of the n-roll game to the list
        return y   # The function returns the list with expected payoffs
