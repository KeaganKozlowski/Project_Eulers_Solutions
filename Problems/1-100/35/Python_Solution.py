from itertools import permutations, product # to generate permutations, im lazy

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def circular(n, primes):
    perms = permutations(str(n))
    counter = 0
    for p in perms:
        if isPrime(int(p)):
            primes.pop(int(p))
            counter += 1
    return counter, primes


primes = []

for i in range(100, 1000000):
    if isPrime(i):
        primes.append(i)

print(len(primes))
print(primes[-1])

circulars = 0
for prime in primes:
    add_circulars, primes = circular(prime, primes)
    circulars += add_circulars
print(circulars)