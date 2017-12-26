#coding:utf8
def lengthOfLIS(nums):
    if not nums:
        return 0

    # l[i]表示以nums[i]（nums[i]一定选取）结尾的上升序列最大长度
    l = [1]*len(nums)
    for i in xrange(1, len(nums)):
        for j in xrange(i):
            if nums[j]<nums[i]:
                l[i] = max(l[i], 1+l[j])

    return max(l)
