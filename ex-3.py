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

def mersenne_test(limit):
    results = []
    for p in range(2, limit+1):
        if is_prime(p):
            m = 2**p - 1
            results.append((p, m, is_prime(m)))
    return results

print(mersenne_test(20))

