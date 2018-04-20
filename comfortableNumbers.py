# --*--coding: utf-8 --*--
"""
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.
How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other?
"""


def comfortableNumbers(l, r):
    c = 0

    def s(x):
        d = 0
        while x:
            d += x % 10
            x /= 10
        return d

    for a in range(l, r):
        for b in range(a + 1, r + 1):
            if (a - s(a)) <= b <= (a + s(a)) and (b - s(b) <= a <= b + s(b)):
                c += 1
    return c


print comfortableNumbers(12, 1000)
