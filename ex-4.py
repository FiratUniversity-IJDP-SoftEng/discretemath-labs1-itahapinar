def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def check_formula():
    results = []
    for n in range(0, 41):
        val = n*n + n + 41
        results.append((n, val, is_prime(val)))
    return results

for r in check_formula():
    print(r)

