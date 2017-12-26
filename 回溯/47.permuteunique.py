#coding:utf8
def permute(nums):
    res = []
    nums.sort()
    dfs(nums, [], res)
    return res
    
def dfs(nums, path, res):
    if len(nums) == 0:
        res.append(path)
        return
    for i in range(len(nums)):
        # 通过下面的语句过滤掉重复元素
        if i!=0 and nums[i-1]==nums[i]:
            continue
        dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
    return
