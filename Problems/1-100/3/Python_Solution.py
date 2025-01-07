def isPrime(n: int) -> bool:
    if n <= 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

largest = 1
for i in range(1,  600851475143 + 1):
    if isPrime(i) and 600851475143 % i == 0 and i > largest:
        largest = i
print(largest)