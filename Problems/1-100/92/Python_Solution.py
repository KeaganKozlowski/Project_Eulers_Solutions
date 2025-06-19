from multiprocessing import Pool

def square(n):
    total = 0
    for e in str(n):
        total += (int(e)**2)
    #print(total)
    return total
def sqaure_digit_chain(n, list):
    if n == 89:
        return True
    if n == 1:
        return False
    k = square(n)
    if list:
        if k in list:
            return False
    #print(list)
    return sqaure_digit_chain(k, list + [k])

def check_chain(n):
    if sqaure_digit_chain(n, []):
        return 1
    return 0

counter = 0
#sqaure_digit_chain(44, [])
#square(44)

#for i in range(1,10000000):
 #   if sqaure_digit_chain(i,[]):
  #      counter += 1

#print(counter)

if __name__ == '__main__':
    with Pool() as pool:
        results = pool.map(check_chain, range(1, 10000000))
    print(sum(results))
