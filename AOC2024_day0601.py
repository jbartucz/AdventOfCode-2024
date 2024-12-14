
path = []
direction = "N"
blocks = set()
height = 0
width = 0
with open("AOC2024_day06.txt") as finpt:
    for i, inpt in enumerate(finpt):
        height += 1
        width = len(inpt.strip())
        for j, c in enumerate(inpt):
            if c == "#":
                blocks.add((i,j))
            if c == "^":
                path.append((i,j))
                current = (i,j)

while True:
    if direction == "N":
        if current[0] == 0:
            break
        elif (current[0] - 1, current[1]) in blocks:
            direction = "E"
            continue
        else:
            current = (current[0] - 1, current[1])
            path.append(current)

    if direction == "S":
        if current[0] == height - 1:
            break
        elif (current[0] + 1, current[1]) in blocks:
            direction = "W"
            continue
        else:
            current = (current[0] + 1, current[1])
            path.append(current)

    if direction == "W":
        if current[1] == 0:
            break
        elif (current[0], current[1] - 1) in blocks:
            direction = "N"
            continue
        else:
            current = (current[0], current[1] - 1)
            path.append(current)

    if direction == "E":
        if current[1] == width - 1:
            break
        elif (current[0], current[1] + 1) in blocks:
            direction = "S"
            continue
        else:
            current = (current[0], current[1] + 1)
            path.append(current)

print(path)
print(len(set(path)))