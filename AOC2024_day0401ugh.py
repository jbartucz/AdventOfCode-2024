import re

res = 0
with open("AOC2024_day04.txt") as finpt:
    vert = []
    for inpt in finpt:
        res += inpt.count("XMAS")
        res += inpt.count("SAMX")

        for i,c in enumerate(inpt):
            if len(vert) <= i:
                vert.append(c)
            else:
                vert[i] += c
    
    print(vert)
    for inpt in vert:
        res += inpt.count("XMAS")
        res += inpt.count("SAMX")



print(res)
