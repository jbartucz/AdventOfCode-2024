
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

def checkheading(loc):

    for block in blocks:

        if loc[2] == "N":
            if block[0] < loc[0] and block[1] == loc[1]:
                return True
        if loc[2] == "S":
            if block[0] > loc[0] and block[1] == loc[1]:
                return True
        if loc[2] == "E":
            if block[0] == loc[0] and block[1] > loc[1]:
                return True
        if loc[2] == "W":
            if block[0] == loc[0] and block[1] < loc[1]:
                return True

    return False

newblocks = set()

for loc in path:
    origloc = loc
    direction = loc[2]
    tempblock = ()

    # try adding a temporary obstacle

    if direction == "N":
        if loc[0] == 0:
            break
        elif (loc[0] - 1, loc[1]) in blocks:
            direction = "E"
            continue
        else:
            if checkheading((loc[0], loc[1],"E")) == True:
                tempblock = (loc[0] - 1, loc[1])
                blocks.add(tempblock)

    elif direction == "S":
        if loc[0] == height - 1:
            break
        elif (loc[0] + 1, loc[1]) in blocks:
            direction = "W"
            continue
        else:
            if checkheading((loc[0], loc[1],"W")) == True:
                tempblock = (loc[0] + 1, loc[1])
                blocks.add(tempblock)

    elif direction == "W":
        if loc[1] == 0:
            break
        elif (loc[0], loc[1] - 1) in blocks:
            direction = "N"
            continue
        else:
            if checkheading((loc[0], loc[1],"N")) == True:
                tempblock = (loc[0], loc[1] - 1)
                blocks.add(tempblock)

    elif direction == "E":
        if loc[1] == width - 1:
            break
        elif (loc[0], loc[1] + 1) in blocks:
            direction = "S"
            continue
        else:
            if checkheading((loc[0], loc[1],"S")) == True:
                tempblock = (loc[0], loc[1] + 1)
                blocks.add(tempblock)

    else:
        print("3 **************************************")


    current = loc
    while True:

        if direction == "N":
            if current[0] == 0:
                break
            elif (current[0] - 1, current[1]) in blocks:
                direction = "E"
                continue
            else:
                current = (current[0] - 1, current[1],direction)

        elif direction == "S":
            if current[0] == height - 1:
                break
            elif (current[0] + 1, current[1]) in blocks:
                direction = "W"
                continue
            else:
                current = (current[0] + 1, current[1],direction)

        elif direction == "W":
            if current[1] == 0:
                break
            elif (current[0], current[1] - 1) in blocks:
                direction = "N"
                continue
            else:
                current = (current[0], current[1] - 1,direction)

        elif direction == "E":
            if current[1] == width - 1:
                break
            elif (current[0], current[1] + 1) in blocks:
                direction = "S"
                continue
            else:
                current = (current[0], current[1] + 1,direction)

        else:
            print("4 **************************************")

        # we found a loop
        if current == origloc:
            newblocks.add(tempblock)
            break

    # remove the temporary obstacle
    if tempblock in blocks:
        blocks.remove(tempblock)

print(newblocks)