'''
n = '+'s
m = '-'s
'''
def PlusXorMinus(n, m):
    if m & 1:
        return -1
    else:
        return 1
