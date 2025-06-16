def score(word, position):
    word.replace('"','')
    total = sum([(ord(e)) - 64 for e in word])
    #print(total)
    if position == 0:
        return 1 * total
    else:
        return (position + 1) * total

file = open("names.txt", "r")
base_line = file.readline()
names = base_line.split(",")
#print(names[0][1])
# Looking at the second element of each string as each string features "," even though it is already type string, so wasted words
names_sorted = sorted(names,key= lambda x: x[1])
#print(score("COLIN", 937))
total = 0
for i, e in enumerate(names_sorted):
    total += score(e, i)
print(total)
