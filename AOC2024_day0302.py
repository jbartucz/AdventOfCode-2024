import re

res = 0
with open("AOC2024_day03.txt") as finpt:
    inpt = ""
    for i in finpt:
        inpt = inpt + i

    start = inpt.find("don't()")
    while start > -1:
        stop = inpt.find("do()",start)
        if stop < 0:
            inpt = inpt[:start]
        else:   
            inpt = inpt[:start] + inpt[stop +4:]
        start = inpt.find("don't()",start)

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", inpt)
    for mul in muls:
        a,b = mul[4:-1].split(",")
        res += int(a) * int(b)

print(res)
