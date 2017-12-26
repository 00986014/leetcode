def rob(self, nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    return max(self.solver(nums[1:]), self.solver(nums[:-1]))       
    
def solver(self, nums):
    n = len(nums)
    l = [-1]*(n+1)
    l[0] = 0
    l[1] = nums[0]        

    i = 2
    while i<=n:
        l[i] = max(l[i-2]+nums[i-1], l[i-1])
        i += 1
    return l[n]
