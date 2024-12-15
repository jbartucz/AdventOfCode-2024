
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
                path.append((i,j,"N"))
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
            path.append((current[0],current[1],direction))

    elif direction == "S":
        if current[0] == height - 1:
            break
        elif (current[0] + 1, current[1]) in blocks:
            direction = "W"
            continue
        else:
            current = (current[0] + 1, current[1])
            path.append((current[0],current[1],direction))

    elif direction == "W":
        if current[1] == 0:
            break
        elif (current[0], current[1] - 1) in blocks:
            direction = "N"
            continue
        else:
            current = (current[0], current[1] - 1)
            path.append((current[0],current[1],direction))

    elif direction == "E":
        if current[1] == width - 1:
            break
        elif (current[0], current[1] + 1) in blocks:
            direction = "S"
            continue
        else:
            current = (current[0], current[1] + 1)
            path.append((current[0],current[1],direction))

    else:
        print("2 **************************************")

# print(path)


newblocks = set()

for pathcount, tempblockloc in enumerate(path):
    print(f"{pathcount} / {len(path)} : {tempblockloc}")
    if pathcount == 0:
        continue

    tempblock = (tempblockloc[0], tempblockloc[1])
    blocks.add(tempblock)

    current = path[0]
    # print(path)
    loopset = set()
    while True:

        # if pathcount == 3:
        #    print(loopset)
        #    print(current)
        #    print()

        direction = current[2]
        loopset.add(current)

        if direction == "N":
            if current[0] == 0:
                break
            elif (current[0] - 1, current[1]) in blocks:
                direction = "E"
                current = (current[0], current[1], "E")
                continue
            else:
                current = (current[0] - 1, current[1],direction)

        elif direction == "S":
            if current[0] == height - 1:
                break
            elif (current[0] + 1, current[1]) in blocks:
                direction = "W"
                current = (current[0], current[1], "W")
                continue
            else:
                current = (current[0] + 1, current[1],direction)

        elif direction == "W":
            if current[1] == 0:
                break
            elif (current[0], current[1] - 1) in blocks:
                direction = "N"
                current = (current[0], current[1], "N")
                continue
            else:
                current = (current[0], current[1] - 1,direction)

        elif direction == "E":
            if current[1] == width - 1:
                break
            elif (current[0], current[1] + 1) in blocks:
                direction = "S"
                current = (current[0], current[1], "S")
                continue
            else:
                current = (current[0], current[1] + 1,direction)

        else:
            print("4 **************************************")

        # we found a loop
        if current in loopset:
            # print(current, loopset)
            newblocks.add(tempblock)
            break

    # remove the temporary obstacle
    blocks.remove(tempblock)

print(newblocks)
print(len(newblocks))