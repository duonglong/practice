import math
def sqrt(N):
    x = 2**math.ceil(N/2)
    while 1:
        y = math.floor((x + math.floor(N/x))/2)
        if y >= x:
            return x
        x = y
print sqrt(1000000000)
