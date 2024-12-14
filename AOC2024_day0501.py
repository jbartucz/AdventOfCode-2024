import re

res = 0
with open("AOC2024_day05.txt") as finpt:
    rules = []
    pagelist = []

    for inpt in finpt:
        if "|" in inpt:
            rules.append([int(x) for x in inpt.split("|")])
        elif len(inpt) > 1:
            pagelist.append([int(x) for x in inpt.split(",")])
    
    middle_sum = 0
    for pages in pagelist:
        pagelist_valid = True
        for r in rules:
            if r[0] not in pages or r[1] not in pages:
                continue

            apos = pages.index(r[0])
            bpos = pages.index(r[1])

            if apos > bpos:
                pagelist_valid = False
                break

        if pagelist_valid == True:
            middle_sum += pages[len(pages)//2]

print(middle_sum)