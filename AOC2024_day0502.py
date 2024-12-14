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
    for i, pages in enumerate(pagelist):

        toadd = False

        done = False
        while done == False:
            done = True
            for r in rules:
                if r[0] not in pages or r[1] not in pages:
                    continue

                apos = pages.index(r[0])
                bpos = pages.index(r[1])

                if apos > bpos:
                    toadd = True
                    pages[apos] = r[1]
                    pages[bpos] = r[0]
                    pagelist[i] = pages
                    done = False # have to check all the rules again

        if toadd == True:
            print(f"*** {pages}")
            middle_sum += pages[len(pages)//2]

print(middle_sum)