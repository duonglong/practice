import math
def numberOfTriangles2(sticks):
    c = 0
    l = len(sticks)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j + 1, l):
                if sticks[i] + sticks[j] > sticks[k]:
                    c += 1
                else:
                    print "%s, %s, %s" % (sticks[i], sticks[j], sticks[k])
    return c

def combination(n, k):
    r = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return r

print combination(5, 3) - 3

print numberOfTriangles2([3, 5, 7, 9, 10])