# coding:utf8
def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    l = [-1]*n

    # l[i]保存考虑从i到n-1的房子
    l[n-1] = nums[n-1]
    for i in xrange(n-2, -1, -1):
        for j in xrange(i, n):
            if j+2<n:
                l[i] = max(l[i], nums[j]+l[j+2])
            else:
                l[i] = max(l[i], nums[j])
    return l[0]


def rob2(nums):
    if not nums:
        return 0
    n = len(nums)
    l = [-1]*n

    # l[i]保存考虑从0到i的房子
    l[0] = nums[0]
    for i in xrange(1, n):
        for j in range(i+1):
            if j>=2:
                l[i] = max(l[i], l[j-2]+nums[j])
            else:
                l[i] = max(l[i], nums[j])
    return l[n-1]


def rob3(nums):
    if not nums:
        return 0
    n = len(nums)
    l = [-1]*(n+1)
    l[0] = 0
    l[1] = nums[0]        

    i = 2
    while i<=n:
        l[i] = max(l[i-2]+nums[i-1], l[i-1])
        i += 1
    return l[n]

def rob4(self, nums):
    last, now = 0, 0     
    for i in nums: 
        last, now = now, max(last + i, now)                
    return now

