
def checkvalid(nums):

    if nums != sorted(nums) and nums != sorted(nums, reverse=True):
        return False

    for i in range(len(nums) - 1):
        diff = abs(nums[i+1] - nums[i])
        if diff > 3 or diff == 0:
            return False

    return True

totalsum = 0

with open("AOC2024_day02.txt") as inpt:
    badlist = []
    for line in inpt:
        nums = [int(x) for x in line.strip().split()]
        #print(nums)

        if checkvalid(nums) == True:
            totalsum += 1
            #print(f"YES {nums}")
        else:
            #print(f"NO  {nums}")
            for i in range(len(nums)):
                newnums = list(nums)
                newnums.pop(i)
                #print(f"TRYING {newnums}")
                if checkvalid(newnums) == True:
                    # print(f"---YES {newnums}")
                    totalsum += 1
                    break


print(totalsum)