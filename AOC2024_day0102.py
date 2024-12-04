

left = []
right = []
with open("AOC2024_day01.txt") as inpt:
    for line in inpt:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

totalsum = 0
for l in left:
    totalsum += l * right.count(l)

print(totalsum)