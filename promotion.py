"""
Product promotion: discount on product
Bundle promotion: Buy product give product

Find all discount combinations

INPUT:
    bundle: {(product, quantity): (bundle_product, bundle_quantity)}
    product: {(product, quantity): discount_amount}
OUTPUT:
    possible discount combinations

EG:
    product(X): {
        (A, 1): 5,
        (A, 2): 7,
        (A, 3): 13,
        (B, 1): 15
    }

    bundle(Y): {
        (A, 1): (B, 1),
        (A, 2): (B, 2),
        (A, 3): (B, 4)
    }

    Order Line: [(A, 13), (B, 7)]



"""

def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    n_1 = solve(n-1)
    n_3 = solve(n-3)
    n_5 = solve(n-5)
    return n_1 + n_3 + n_5
print solve(6)