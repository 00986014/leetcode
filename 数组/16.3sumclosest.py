def threeSumClosest(nums, target):
    nums.sort()
    result = float('inf')
    for i in xrange(len(nums)-2):
        if i==0 or (i>0 and nums[i] != nums[i-1]):
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[i] == target:
                    return target
                if abs(nums[l]+nums[r]+nums[i]-target)<abs(result-target):
                    result = nums[l]+nums[r]+nums[i]
                if nums[l]+nums[r]+nums[i]<target:
                    l += 1
                elif nums[l]+nums[r]+nums[i]>target:
                    r -= 1
    return result
