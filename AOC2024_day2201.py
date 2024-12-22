
def doit(num):

    for i in range(2000):
        res = num * 64
        num = num ^ res
        num = num % 16777216

        res = num // 32
        num = num ^ res
        num = num % 16777216

        res = num * 2048
        num = num ^ res
        num = num % 16777216

        # print(num)

    return num


totalsum = 0
with open("AOC2024_day22.txt") as finpt:
    for inpt in finpt:
        current = int(inpt)
        totalsum += doit(current)

print(totalsum)

