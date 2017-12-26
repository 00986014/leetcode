def twoSunm(nums, target):
    d = {}
    for i in xrange(len(nums)):
        if (target - nums[i]) in d:
            return (d[target - nums[i]],i)
        d[nums[i]] = i
        
