
def d(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total

print(d(220))
print(d(284))

total = 0
for a in range(1, 10000):
    b = d(a)
    if a == d(b) and a != b:
        print(a,b)
        total += a

#total += 220
#total += 284
print(total)