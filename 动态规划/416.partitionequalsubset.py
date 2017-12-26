#coding:utf8
def canPartition(nums):
    c = sum(nums)
    if c%2 != 0:
        return False
    else:
        c /= 2

    #l[i][c]表示使用索引为[0-i]的元素是否可以完全填充一个容量为c的背包
    #-1表示未计算，0表示不可以，1表示可以 
    l = []
    for i in xrange(len(nums)):
        l.append([-1]*(c+1))
        
    return tryPartition(nums, c, len(nums)-1, l)


def tryPartition(nums, c, index, l):
    if c == 0:
        return True

    if c<0 or index<0:
        return False

    if l[index][c] != -1:
        return l[index][c] == 1

    if tryPartition(nums, c, index-1, l) or \
       tryPartition(nums, c-nums[index], index-1, l):
        l[index][c] = 1
    else:
        l[index][c] = 0

    return l[index][c] == 1


def canPartition2(nums):
    c = sum(nums)
    if c%2 != 0:
        return False
    else:
        c /= 2

    n = len(nums)
    # l[i]存放容量为i的背包能否存满
    l = [False]*(c+1)

    # 先把nums[0]放进合适容量的背包中
    for i in xrange(c+1):
        l[i] = (nums[0]==i)

    # 对于每个新元素nums[i]，在已有前面元素的情况下，
    # 考虑其能否充满从c到nums[i]容量的背包中。
    # 不用考虑容量小于nums[i]的背包，因为肯定放不进。
    for i in xrange(1, n):
        for j in xrange(c, nums[i]-1, -1):
            l[j] = l[j] or l[j-nums[i]]

    return l[c]
    
