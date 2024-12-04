
def checkvalid(nums):

    dir = 0
    if nums == sorted(nums):
        dir = 1
    elif nums == sorted(nums, reverse=True):
        dir = -1
    else:
        return False

    for i in range(len(nums) - 1):
        diff = abs(nums[i+1] - nums[i])
        if diff > 3 or diff == 0:
            return False
            


totalsum = 0

with open("AOC2024_day02.txt") as inpt:
    badlist = []
    for line in inpt:
        numss = line.strip().split()
        nums = []
        for n in numss:
            nums.append(int(n))
        print(nums)

        dir = 0
        if nums == sorted(nums):
            dir = 1
        elif nums == sorted(nums, reverse=True):
            dir = -1
        else:
            badlist.append(nums)
            continue # not in order

        numbad = 0
        allbad = False
        for i in range(len(nums) - 1):
            diff = abs(nums[i+1] - nums[i])
            if diff > 3 or diff == 0:
                if numbad > 0:
                    allbad = True
                    break
                else:
                    numbad += 1
                    testnums = list(nums)
                    testnums.pop(i)
                    if checkvalid(testnums) == False:
                        allbad = True
                        break
        
        if allbad == False and numbad > 0:
            print(f"* {nums}")

        if allbad == False:
            totalsum += 1


print(totalsum)