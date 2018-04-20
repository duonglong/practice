def binomialCoeff(n, k):
    """
    Return binomial coefficient C(n,k)
    """
    if k == 0 or k == n:
        return 1
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)
