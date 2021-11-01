def cost(B):
    print(B)
    if len(B) == 2:
        return max(B) - 1
    c_next = cost(B[1:])
    m = c_next if c_next > B[1] else B[1]
    k = m if m > B[0] else B[0] - 1
    print(c_next, m, k)
    return c_next + k


print(cost([10, 1, 10, 1]))
# print(cost([5, 3, 2]))
# print(cost([3,5,2]))
# print(cost([100, 2, 100, 2, 100]))
