def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    index = 1
    while i < len(nums)-1:
        if nums[i] == nums[i+1] and index == 0:
            nums.pop(i)
        elif nums[i] == nums[i+1] and index !=0:
            index = 0
            i += 1
        else:
            index = 1
            i += 1
    return (i+1)
