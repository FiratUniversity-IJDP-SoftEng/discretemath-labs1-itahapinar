import random

def is_probable_prime(n, k=8):
    if n < 2:
        return False

    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_100_digit_primes(count=10):
    primes = []
    lower = 10**99
    upper = 10**100 - 1

    while len(primes) < count:
        candidate = random.randint(lower, upper)
        if is_probable_prime(candidate):
            primes.append(candidate)

    return primes

print(generate_100_digit_primes())

