def curious_number(n):
    total = 0
    for e in str(n):
        total += factorial(int(e))
    if n == total:
        return True
    else:
        return False

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

sum = 0
for i in range(10,  2540160 + 1): # All single digits numbers are excluded and 9! = 2540160
    if curious_number(i):
        sum += i
print(sum)