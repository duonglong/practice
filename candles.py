def candles(candles, makeNew):
    res = 0
    leftovers = 0
    while candles:
        res += candles
        leftovers += candles
        remain = leftovers % makeNew
        candles = leftovers / makeNew
        leftovers = remain
    return res
def candles2(c,m):
    r = c + ((c-m)/(m-1)) + 1
    #r = (c * m - 1)/ (m - 1)
    return r
k = 4
j = 1
for i in range(k, 25):
    print "%s -> (%s, %s): %s, %s" % (j, i, k, candles(i,k), candles2(i, k))
    j += 1
