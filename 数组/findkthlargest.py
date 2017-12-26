def findKthLargest(nums, k):
    left = -1
    right = len(nums)
    mid = 0
    partition = nums[0]
    while mid<right:
        if nums[mid] < partition:
            left += 1
            nums[left], nums[mid] = nums[mid], nums[left]
            mid += 1
        elif nums[mid] > partition:
            right -= 1
            nums[mid], nums[right] = nums[right], nums[mid]
        else:
            mid += 1
    mid -= 1
    #print mid, nums, k, nums[mid]
    if mid == len(nums)-k:
        return nums[mid]
    elif mid < len(nums)-k:
        return findKthLargest(nums[mid+1:], k)
    else:
        return findKthLargest(nums[:mid], k-(len(nums)-mid))
