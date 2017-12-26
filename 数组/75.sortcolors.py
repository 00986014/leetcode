def sortColors(nums):
    l = [0, 0, 0]
	for i in nums:
		l[i] += 1
	index = 0
	for i in xrange(len(l)):
		for j in xrange(l[i]):
			nums[index] = i
			index += 1

