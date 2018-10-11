"""
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N'
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

Total number of ways to form 6 is : 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1
"""

def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return solve(n-1) + solve(n-3) + solve(n-5)

print solve(7)
#
# N=1: 1
# N=2: 1
# N=3: 2 (1,1,1; 3)
# N=4: 3 (1,1,1,1; 1,3; 3,1)
# N=5: 5 (1,1,1,1,1; 1,1,3; 1,3,1; 3,1,1; 5)