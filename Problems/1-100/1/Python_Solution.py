def by5(n: int) -> bool:
    return n % 5 == 0

def by3(n: int) -> bool:
    return n % 3 == 0

total_sum = 0
for i in range(1000):
    if by5(i) or by3(i):
        total_sum += i

print(total_sum)