
totalsum = 0

with open("AOC2024_day02.txt") as inpt:
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
            continue # not in order

        bad = False
        for i in range(len(nums) - 1):
            diff = abs(nums[i+1] - nums[i])
            if diff > 3 or diff == 0:
                bad = True
                # print(f"{diff} {i} {nums[i]} {nums[i+1]} : {line.strip()}")
                break

        if bad == False:
            totalsum += 1


print(totalsum)