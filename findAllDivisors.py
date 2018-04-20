def findAllDivisors(n):
    divisors = [1]
    for i in range(2, n / 4):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return list(set(sorted(divisors)))

print findAllDivisors(220)