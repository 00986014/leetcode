def containNearbyDuplicate(nums, k):
    A = set()
    for i in xrange(len(nums)):
        if nums[i] in A:
            return True
        A.add(nums[i])
        if len(A) == k+1:
            A.remove(nums[i-k])
    return False
