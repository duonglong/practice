import math
def p(x):
    x = 1.0 + 1.0 / x
    print x
    return x


x = (1 - math.sqrt(5)) / 2
for i in range(1, 100):
    x = p(x)
print '-----------------------'