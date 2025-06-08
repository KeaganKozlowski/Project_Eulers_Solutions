# Read file
file = open("100-50_digit_numbers.txt", "r")
total_sum = 0
for line in file:
    total_sum += int(line)

print(total_sum)
print(str(total_sum)[:10])
print(len(str(total_sum)[:10]))
