# --*--coding: utf-8 --*--
import math
import time

def combination(n, k):
    r = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print "n: %s, k: %s, r: %s" % (n, k, r)
    return r


def permutation_order(n, k):
    # P(n+k−1,k)

    r = math.factorial(n + k - 1) / math.factorial(k)
    print "n: %s, k: %s, r: %s" % (n, k, r)
    return r


def permutation(n, k):
    if k == 0:
        return 0
    if n == k:
        return 1
    r = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    # print "n: %s, k: %s, r: %s" % (n, k, r)
    return r


def climb(n):
    """

    :param n: number of stairs
    :return: number of ways to climb n stair
    """
    r = 1
    for i in range(n / 2 + 1):
        r += permutation(n - i, i)
    return r

hash_table = {}
def recursive_fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in hash_table:
        return hash_table[n]
    else:
        r = recursive_fib(n - 1) + recursive_fib(n - 2)
        hash_table[n] = r
        return r

def fibonacci(n):
    a = 1
    b = 2
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

start = time.time()
print recursive_fib(1000)
print time.time() - start
# print climb(7)
# start = time.time()
# climb(1000)
# t_climb = time.time() - start
start = time.time()
print fibonacci(1000)
t_fib = time.time() - start
print t_fib
# print t_climb
# print "t_climb: %s, t_fib: %s" % (t_climb, t_fib)

# for x in range(100):
#     a, b = climb(x), fibonacci(x + 2)
#     print "%s, %s, %s" % (x, a, b)


# n = 1 (1) => 1
# n = 2 (1,1) (2) => 2
# n = 3 (1,1,1) (1,2) (2,1) => 3
# n = 4 (1,1,1,1) (2,1,1) (1,2,1) (1,1,2) (2,2) => 5
# n = 5 (1,1,1,1) (2,1,1,1) (1,2,1,1) (1,1,2,1) (1,1,1,2) (1,2,2) (2,1,2) (2,2,1) => 8
# n = 6 (1,1,1,1,1,1) (1,2,1,1,1) (1,1,2,1,1) (1,1,1,2,1) (1,1,1,1,2) (1,2,2,1) (1,2,1,2) (1,1,2,2) (2,2,2)