def ispowerof2(v):
    return v and not (v & (v - 1));


def lognbase2(v):
    #
    MultiplyDeBruijnBitPosition = [
        0, 9, 1, 10, 13, 21, 2, 29, 11, 14, 16, 18, 22, 25, 3, 30,
        8, 12, 20, 28, 15, 17, 24, 7, 19, 27, 23, 6, 26, 5, 4, 31
    ]
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    index = (v * 0x07C4ACDD) >> 27
    r = MultiplyDeBruijnBitPosition[index]
    return r


for i in range(0, 32):
    print '%s: %s' % (i, lognbase2(i))
