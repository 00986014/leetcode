#coding:utf8
def containNearbyAlmostDuplicate(nums, k, t):
    if t < 0:
        return False
    d = {}
    w = t + 1
    # 将数组中的元素按照t+1的宽度分成若干个桶，如果两个元素之差在t以内，则要么在
    # 一个桶内，要么在相邻桶内
    for i in xrange(len(nums)):
        m = nums[i] / w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
            return True
        d[m] = nums[i]
        if i >= k:
            del d[nums[i - k] / w]
    return False
