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

def pseudoprimes_base_2(limit=10000):
    numbers = []
    for n in range(2, limit+1):
        if not is_prime(n): 
            if pow(2, n-1, n) == 1:
                numbers.append(n)
    return numbers

print(pseudoprimes_base_2())

