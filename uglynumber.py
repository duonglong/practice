"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
"""


def uglynumber(n):
    ugly_1st = 1

    uglies_2 = [2]
    uglies_3 = [3]
    uglies_5 = [5]

    for i in range(1, n + 2):
        pass
