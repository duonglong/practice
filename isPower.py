import math
def isPower(n):
    for i in range(2, n + 1):
        k = n**(1.0/i)
        if round(k,14) == int(round(k, 14)) :
            return True
    return False

for i in range(1, 351):
    print i, isPower(i)