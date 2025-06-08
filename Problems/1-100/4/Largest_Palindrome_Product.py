def largest_palindrome_product(minimum, maximum):
    palis = []
    for num in range(minimum, maximum+1):
        for product in range(minimum, num+1):
            prod = product*num
            if str(prod)==str(prod)[::-1]:
                palis.append(product)
    return palis[-1]

print(largest_palindrome_product(100,999))