import re

res = 0
with open("AOC2024_day04.txt") as finpt:
    chars = []
    for inpt in finpt:
        lst = [c for c in inpt.strip()]
        chars.append(lst)

    for i in range(len(chars)):
        for j in range(len(chars[0])):
            if i < len(chars[0]) - 3:
                if chars[j][i] + chars[j][i+1] + chars[j][i+2] + chars[j][i+3] == "XMAS":
                    res += 1
                if chars[j][i] + chars[j][i+1] + chars[j][i+2] + chars[j][i+3] == "SAMX":
                    res += 1
            if j < len(chars) - 3:
                if chars[j][i] + chars[j+1][i] + chars[j+2][i] + chars[j+3][i] == "XMAS":
                    res += 1
                if chars[j][i] + chars[j+1][i] + chars[j+2][i] + chars[j+3][i] == "SAMX":
                    res += 1
            if i < len(chars[0]) - 3 and j < len(chars) - 3:
                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] + chars[j+3][i+3] == "XMAS":
                    res += 1
                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] + chars[j+3][i+3] == "SAMX":
                    res += 1
            if i > 2 and j < len(chars) - 3:
                if chars[j][i] + chars[j+1][i-1] + chars[j+2][i-2] + chars[j+3][i-3] == "XMAS":
                    res += 1
                if chars[j][i] + chars[j+1][i-1] + chars[j+2][i-2] + chars[j+3][i-3] == "SAMX":
                    res += 1



print(res)
