def topFrequent(nums, k):
    from collections import Counter
    d = Counter(nums)

    from Queue import PriorityQueue
    q = PriorityQueue()

    for key, value in d.iteritems():
        if q.qsize() == k:
            q.put([value, key])
            q.get()
        else:
            q.put([value, key])
    
    result = []
    while q.qsize() != 0:
        fre = q.get()
        result.append(fre[1])

    return result[::-1]
