

def rec(lst):

    toreturn = set()
    if len(lst) == 1:
        toreturn.add(lst[0])
        return toreturn
    
    vals = rec(lst[:-1])
    for v in vals:
        toreturn.add(v * lst[-1])
        toreturn.add(v + lst[-1])
    return toreturn

def squeezerec(lst):

    toreturn = list()
    if len(lst) == 2:
        toreturn.append([lst[0],lst[1]])
        toreturn.append([int(str(lst[0])+str(lst[1]))])
        return toreturn
    
    vals = squeezerec(lst[:-1])
    for v in vals:
        toreturn.append(v + [lst[-1]])
        toreturn.append(v[:-1] + [int(str(v[-1])+str(lst[-1]))])
    return toreturn

totalsum = 0
with open("AOC2024_day07.txt") as finpt:
    for inpt in finpt:
        sum, nums = inpt.split(": ")
        sum = int(sum)
        nums = [int(n) for n in nums.split()]
        allthelists = squeezerec(nums)
        for lst in squeezerec(nums):
            if sum in rec(lst):
                totalsum += sum


print(totalsum)