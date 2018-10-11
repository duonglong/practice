
def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return solve(n - 1) + solve(n - 3) + solve(n - 5)


array = [1, 3, 5]

def solve2(n):
    count = []
    for i in range(n + 1):
        count.append(0)
    count[0] = 1

    for i in range(1, n + 1):
        for j in range(len(array)):
            if i >= array[j]:
                count[i] += count[i - array[j]]

    return count[n]


print solve(30), solve2(30)