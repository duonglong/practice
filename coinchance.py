
def getWays(n, c):
    m = {k: 0 for k in range(n+1)}
    m[0] = 1
    for coin in c:
        for i in range(1, n+1):
            if coin <= i:
                m.setdefault(i, 0)
                m.setdefault(i - coin, 0)
                m[i] += m[i - coin]
    return m[n]

n = 1
c = [48, 6, 34, 50, 49, 36, 30, 35, 40, 41, 17, 43, 39, 13, 4, 20, 19, 2, 46, 7, 38, 33, 28, 18, 21]
getWays(n, c)
