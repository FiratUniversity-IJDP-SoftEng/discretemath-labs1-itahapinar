def prime(n):
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

def listofprimes(n):
    primes = []
    for k in range(2, n+1):
        if prime(k):
            primes.append(k)
    return primes

print(listofprimes(50))

