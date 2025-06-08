# Read file
file = open("Problems/1-100/13/100-50_digit_numbers.txt", "r")
total_sum = 0
for line in file:
    total_sum += int(line)

print(total_sum)
