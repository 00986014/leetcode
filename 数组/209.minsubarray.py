def minSubArrayLen(s, nums):
    l, r = 0, -1
    d = 0
    result = len(nums)+1

    while l<len(nums):
        if r+1 < len(nums) and d<s:
            r += 1
            d += nums[r]
        else:
            d -= nums[l]
            l += 1

        if d >= s:
            result = min(result, r-l+1)

    if result == len(nums)+1:
        return 0
    return result
