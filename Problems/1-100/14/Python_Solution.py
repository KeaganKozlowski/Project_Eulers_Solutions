def Odd(num):
    if num%2 == 0:
        return False
    return True

def collatz_sequence(n, counter, actn):
    if n == 1:
        return [actn, counter]
    if Odd(n):
        return collatz_sequence(3*n+1, counter + 1, actn)
    else:
        return collatz_sequence(n//2, counter + 1, actn)

lengths = []
for num in range(1, 1000000):
    lengths.append(collatz_sequence(num, 1, num))

sorted_lengths = sorted(lengths, key = lambda x: x[1], reverse = True)
print(sorted_lengths[0]) # Number, counter

