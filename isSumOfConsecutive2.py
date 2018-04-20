import math


def isSumOfConsecutive2(n):
    if n == 1:
        return 0
    c = 0
    r = int(math.ceil(float(n) / 2)) + 1
    for i in range(1, r):
        total = 0
        for j in range(i, r):
            total += j
            if total == n:
                c += 1
            if total > n:
                continue
    return c


for k in range(1, 100):
    print '%s: %s' % (k, isSumOfConsecutive2(k))