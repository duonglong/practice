friendly_numbers = lambda x, y: "No" if sum(
    x / i * i / x * i - y / i * i / y * i for i in range(1, x + y)) or x == y else "Yes"

friendly_numbers(220, 289)