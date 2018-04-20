def secondRightmostZeroBit(n):
    c = i = 0
    while n:
        if not (n & 1):
            c +=1
        if c == 2:
            return i
        n >>= 1
        i += 1
    return False

def secondRightmostZeroBit2(n):
    return ((~n&(n+1)) + (n + 1)) & (-((~n&(n+1)) + (n + 1)))

for i in range(10, 99):
    # print "%s\n%s"%(bin(i),bin(~i))
    print '%s: %s -> %s, %s' % (i,bin(i)[2:], 2**secondRightmostZeroBit(i), secondRightmostZeroBit2(i))