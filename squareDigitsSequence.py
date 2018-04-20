def squareDigitsSequence(a0):
    l = [a0]
    c = 0
    while 1:
        n = 0
        while a0:
            n += (a0 % 10) ** 2
            a0 /= 10

        if n not in l:
            c += 1
            a0 = n
            l.append(n)
        else:
            break
    return len(l) + 1


print squareDigitsSequence(16)