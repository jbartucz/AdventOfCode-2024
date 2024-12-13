import re

res = 0
with open("AOC2024_day03.txt") as finpt:
    for inpt in finpt:


        muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", inpt)
        for mul in muls:
            a,b = mul[4:-1].split(",")
            res += int(a) * int(b)

print(res)
