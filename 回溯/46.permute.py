def permute(self, nums):
    self.res = []
    self.dfs(nums, [])
    return self.res
    
def dfs(self, nums, path):
    if len(nums) == 0:
        self.res.append(path)
        return
    for i in range(len(nums)):
        self.dfs(nums[:i] + nums[i+1:], path + [nums[i]])
    return
