def score(name):
    return sum([(ord(char) - 64) for char in name])

file = open("names.txt", "r")
base_line = file.readline()

# Sorting names and striping
names = [name.strip('"') for name in base_line.split(",")]
names = sorted(names)

total = 0
for i, e in enumerate(names):
    total += (score(e) * (i + 1))

print(total)

