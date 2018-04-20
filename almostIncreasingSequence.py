def almostIncreasingSequence(sequence):
    prev = sequence[0]
    c = 0
    l = len(sequence) - 3
    for i in sequence[1:l]:
        next = sequence[i + 1]
        # if (prev > i and next > i) or (prev < i and next < i) or (prev == i) or (next == i):
        #     c += 1
        # if c > 1:
        #     return False
    return True


testcases = [
    [1, 3, 2, 1],  # False
    [1, 3, 2],  # True: [1,2] [1,3]
    [1, 2, 1, 2],  # False
    [1, 4, 10, 4, 2],  # False
    [10, 1, 2, 3, 4, 5],  # [1, 2, 3, 4, 5]
    [1, 1, 1, 2, 3],  # False
    [0, -2, 5, 6],  # True: [0, 5, 6] [-2, 5, 6]
    [1, 2, 3, 4, 5, 3, 5, 6],  # False
    [40, 50, 60, 10, 20, 30],  # False
    [1, 1],  # True
    [10, 1, 2, 3, 4, 5, 6, 1],  # False
    [1, 2, 3, 4, 3, 6],  # [1, 2, 3, 4, 6]
    [1, 2, 3, 4, 99, 5, 6]  # [1, 2, 3, 4, 5, 6]
]

for test in testcases:
    print test
    print almostIncreasingSequence(test)
    print "============================="

"""
- Big number in middle
- Small number in middle
- Big Number index is 0
- Small Number index is length -1
- Adj duplicate number
"""
