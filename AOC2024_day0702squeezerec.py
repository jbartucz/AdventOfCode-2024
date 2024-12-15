

def rec(lst):

    toreturn = set()
    if len(lst) == 1:
        toreturn.add(lst[0])
        return toreturn
    
    vals = rec(lst[:-1])
    for v in vals:
        toreturn.add(v * lst[-1])
        toreturn.add(v + lst[-1])
        toreturn.add(int(str(v) + str(lst[-1])))
    return toreturn

totalsum = 0
with open("AOC2024_day07.txt") as finpt:
    for inpt in finpt:
        sum, nums = inpt.split(": ")
        sum = int(sum)
        nums = [int(n) for n in nums.split()]
        if sum in rec(nums):
            totalsum += sum


print(totalsum)