from multiprocessing import Pool
def square_digit_chain(n):
    while n != 1 or n != 89:
        n = sum(int(e)**2 for e in str(n))
    return n

def check(n):
    return 1 if square_digit_chain(n) == 89 else 0

if __name__ == '__main__':
    with Pool() as pool:
        results = pool.map(check, range(1, 10000000))
    print(sum(results))