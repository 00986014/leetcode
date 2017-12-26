def combinationSum3(k, n):
    result = []
    if k == 0 or k > 9 or n <= 0 or n > 45:
        return []
    nums = range(1,10)
    generateCombination(k, n, nums, [], result)
    return result


def generateCombination(k, n, nums, s, result):
    if n == 0 and k==0:
        result.append(s[:])
        return

    if n<0 or k==0 or not nums:
        return

    for i in xrange(len(nums)):
        if nums[i]<=n:
            s.append(nums[i])
            generateCombination(k-1, n-nums[i], nums[i+1:], s, result)
            s.pop()
    return
