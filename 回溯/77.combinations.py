def combine(n, k):
    if n <= 0 or k <= 0 or k > n:
        return []
    result = []
    nums = range(1, n+1)
    
    def generateCombinations(nums, k, c):
        if k == 0:
            result.append(c[:])
            return

        for i in range(len(nums)):
            c.append(nums[i])
            generateCombinations(nums[i+1:], k-1, c)
            c.pop()
        return

    if k > n/2:
        generateCombinations(nums, n-k, [])
        for j in xrange(len(result)):
            result[j] = list(set(nums)-set(result[j]))
    else:
        generateCombinations(nums, k, [])
    return result



