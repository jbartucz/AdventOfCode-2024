import re

res = 0
with open("AOC2024_day04.txt") as finpt:
    chars = []
    for inpt in finpt:
        lst = [c for c in inpt.strip()]
        chars.append(lst)

    for j in range(len(chars)):
        for i in range(len(chars[0])):
            if i < len(chars[0]) - 2 and j < len(chars) - 2:
                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] == "MAS" and chars[j][i+2] + chars[j+1][i+1] + chars[j+2][i] == "MAS":
                    res += 1
                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] == "SAM" and chars[j][i+2] + chars[j+1][i+1] + chars[j+2][i] == "SAM":
                    res += 1

                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] == "MAS" and chars[j+2][i] + chars[j+1][i+1] + chars[j][i+2] == "MAS":
                    res += 1
                if chars[j][i] + chars[j+1][i+1] + chars[j+2][i+2] == "SAM" and chars[j+2][i] + chars[j+1][i+1] + chars[j][i+2] == "SAM":
                    res += 1


print(res)
