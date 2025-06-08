def factorial(n, prod):
    if n == 1:
        return prod
    return factorial(n-1, prod * n)

k = factorial(100, 1)
print(k)
total_sum = 0
for e in str(k):
    total_sum += int(e)
print(total_sum)