def combinationSum4(nums, target):
    if not nums:
        return 0

    nums.sort()
    if target<nums[0]:
        return 0

    n = len(nums)
    l = [0]*(target+1)
    l[0] = 1

    for i in xrange(nums[0], target+1):
        for j in xrange(n):
            if nums[j]<=i:
                l[i] += l[i-nums[j]]

    return l[target]
