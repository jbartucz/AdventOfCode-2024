

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
for i in range(len(left)):
    totalsum += abs(left[i] - right[i])

print(totalsum)