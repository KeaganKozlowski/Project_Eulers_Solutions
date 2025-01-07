def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def iseven(n: int) -> bool:
    return n % 2 == 0

total = 0
print(fib(100))