# We are using a binoial Coefficent

def binomial(n, k):
    nex = ex(n)
    kex = ex(k)
    return nex/(kex*kex)

def ex(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

print(binomial(40,20))