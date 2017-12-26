def subsets(nums):
    if not nums:
        return []
    result = []
    k = len(nums)
    generatesubset(nums, k, [], result)
    return result


def generatesubset(nums, k, s, result):
    if k == 0:
        result.append(s)
        return

    for i in xrange(len(nums)):
        generatesubset(nums[i+1:], k-1, s+[nums[i]], result)
        generatesubset(nums[i+1:], k-1, s, result)
    return


def subsets2(self, nums):
    l = []
    size = len(nums)
    n = 0
    while n<=2**size-1:
        b = bin(n)[2:]
        n += 1
        l.append([])
        for i in range(len(b)):
            if b[::-1][i] == '1':
                l[-1].append(nums[i])
    return l


