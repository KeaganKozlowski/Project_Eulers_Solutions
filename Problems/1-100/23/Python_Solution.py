def d(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total

def is_sum(n, abundants):
    p1, p2 = 0, len(abundants) - 1
    while p1 < p2:
        k = abundants[p1] + abundants[p2]
        if k == n:
            return True
        else:
            if k > n:
                p2 -= 1
            else:
                p1 += 1
    return False

abundants = []
total = 0
for i in range(1,28123):
    if d(i) > i:
        abundants.append(i)
        if not is_sum(i, abundants):
            total += i
print(total)
