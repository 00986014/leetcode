#coding:utf8
def subsetsWithDup(nums):
    nums.sort()
    ans = [[]]
    last = [[]]
    for i, n in enumerate(nums):
        pickFrom = ans
        # 如果遇上相同元素，则pickfrom取上次添加进来的数组，不然会造成重复
        if i!=0 and nums[i-1] == n: 
            pickFrom = last
            
        # 对pickfrom中每个元素加上[n]
        last = [ a + [n] for a in pickFrom ]
        ans += last


    return ans
