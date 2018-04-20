import numpy
from numpy.random import randn

def _normal_distribute(n):
    c = len([1 for x in randn(n) if -1 <= x <= 1])
    return float(c) / n * 100

print _normal_distribute(10)
print _normal_distribute(100)
print _normal_distribute(1000)
print _normal_distribute(10000)
print _normal_distribute(100000)
print _normal_distribute(1000000)
print _normal_distribute(10000000)