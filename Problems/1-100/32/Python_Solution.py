def multiplicand(n):
    p1 = 1
    p2 = n
    while p1 != p2:
        if n / p1 == p2:
            if pandigital(str(p1)+str(p2)+str(n)):
                return True
        if p1 + 1 == p2:
            p1, p2 = p1 +1, n
        else:
            p2 -= 1
    return False
    ##


def pandigital(n):
    n = list(n)
    for i in range(1,n+1):
        if i not in n:
            return False
    return True

total = 0
for i in range(1,123456789):
    if multiplicand(i):
        total += 1
